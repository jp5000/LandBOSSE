import re

import pandas as pd
import numpy as np

from .XlsxOperationException import XlsxOperationException
from .WeatherWindowCSVReader import read_weather_window
from ..model import DefaultMasterInputDict
from .GridSearchTree import GridSearchTree


class XlsxReader:
    """
    This class is for reading input data from .xlsx files.

    There are two sets of data to be read from .xlsx files. The first set
    of data is read from the following sheets:

    - components

    - cable_specs

    - equip

    - crane_specs

    - development

    - crew_price

    - crew

    - equip_price

    - material_price

    - rsmeans

    - site_facility_building_area

    - weather_window

    The second set of data are read from a single sheet as described below.

    The first set of data represent a database used by the various modules. Queries
    on these data allow calculation based on labor, material, crane capacity
    and so on. These data can be shared among different projects. These data
    are called project_data.

    The second set of data represent the parameters specific to each project.
    These parameters include things values like hub height, rotor diameter,
    etc. These data are particular to a single project. These data are
    referred to as the project.

    This class also handles modifications of project data dataframes for
    parametric runs and all the other dataframe manipulations that make that
    possible.
    """

    def create_parametric_value_list(self, parametric_list):
        """
        Assuming we have a "Parametric list" sheet/dataframe like the following

        | Project ID | Dataframe name       | Row name | Column name | Start | End | Step
        |------------|----------------------|----------|-------------|-------|-----|------
        | project1   | alpha                | fizz     | buzz        | 0     | 12  | 6
        | project1   | beta                 | foo      | bar         | 0     | 12  | 6
        | project2   | gamma                | dogs     | cats        | 21    | 27  | 3

        Translate this data frame into a data frame of the following format:

        | Project ID | Serial      | alpha/fizz/buzz | beta/foo/bar | gamma/dogs/cats
        |------------|-------------|-----------------|--------------|----------------|
        | project1   | project1_00 | 0               | 0            | NaN            |
        | project1   | project1_01 | 0               | 6            | NaN            |
        | project1   | project1_02 | 0               | 12           | NaN            |
        | project1   | project1_03 | 6               | 0            | NaN            |
        | project1   | project1_04 | 6               | 6            | NaN            |
        | project1   | project1_05 | 6               | 12           | NaN            |
        | project1   | project1_06 | 12              | 0            | NaN            |
        | project1   | project1_07 | 12              | 6            | NaN            |
        | project1   | project1_08 | 12              | 12           | NaN            |
        | project2   | project2_09 | NaN             | NaN          | 21             |
        | project2   | project2_10 | NaN             | NaN          | 24             |
        | project2   | project2_11 | NaN             | NaN          | 27             |

        Here NaN is not an error. It is the normal way Pandas handles
        empty cells It means that, for a particular project,
        to the dataframe/row/column is needed and that the value in that
        dataframe cell should remain unchanged.

        Also, note that the serial numbers are strings that should be left
        padded with zeros. The left padding means that when the strings are
        sorted alphabetically, they will end up in the same order as numeric
        sorting.

        Parameters
        ----------
        parametric_list : pandas.DataFrame
            The first dataframe shown above.

        Returns
        -------
        pandas.DataFrame
            The second dataframe shown above.
        """

        # If the parametric_list is empty, this probably means the sheet
        # that had the parametric values is empty.
        if parametric_list.empty:
            return pd.DataFrame([
                {
                    'Project ID': None,
                    'Serial': None
                }
            ])

        all_parametric_value_rows = []

        # Group all the projects by their ID and iterate over each group
        group_by_project = parametric_list.groupby('Project ID')
        for name, group in group_by_project:

            # For each group/project ID, build a new grid search tree
            grid_search_tree = GridSearchTree(group)
            grid = grid_search_tree.build_grid_tree_and_return_grid()

            # After the tree is built, make new rows that have individual
            # parametric values.
            #
            # A grid_point is set of cell specifications and their values.
            # given our example above, a grid point would be a list of
            # dictionaries about dataframe cells to modify.
            #
            # Grid point 0: alpha/fizz/buzz = 0, beta/foo/bar = 0
            # Grid point 1: alpha/fizz/buzz = 0, beta/foo/bar = 6
            # etc
            parametric_value_rows = []
            for grid_point in grid:
                parametric_value_row = dict()
                for axis in grid_point:
                    parametric_value_row[axis['cell_specification']] = axis['value']
                parametric_value_rows.append(parametric_value_row)

            # Assign the project ID to each row. Because of the grouping,
            # tha name is the same as the project ID.
            for parametric_value_row in parametric_value_rows:
                parametric_value_row['Project ID'] = name

            # Add all these new rows into the master list before
            # iterating again.
            all_parametric_value_rows.extend(parametric_value_rows)

        # Create project names with serial numbers for each row
        for index, parametric_value_row in enumerate(all_parametric_value_rows):
            project_id = parametric_value_row['Project ID']
            serial = self.create_serial_number(project_id, index, len(all_parametric_value_rows))
            parametric_value_row['Serial'] = serial

        # Make a dataframe out of the list of dictionaries. This will
        # add NaN where appropriate

        result = pd.DataFrame(all_parametric_value_rows)

        return result

    def outer_join_projects_to_parametric_values(self, project_list, parametric_value_list):
        """
        Consider the dataframe we made in create_parametric_value_list.
        Call it parametric_value_list:

        | Project ID | Serial      | alpha/fizz/buzz | beta/foo/bar | gamma/dogs/cats
        |------------|-------------|-----------------|--------------|----------------|
        | project1   | project1_00 | 0               | 0            | NaN            |
        | project1   | project1_01 | 0               | 6            | NaN            |
        | project1   | project1_02 | 0               | 12           | NaN            |
        | project1   | project1_03 | 6               | 0            | NaN            |
        | project1   | project1_04 | 6               | 6            | NaN            |
        | project1   | project1_05 | 6               | 12           | NaN            |
        | project1   | project1_06 | 12              | 0            | NaN            |
        | project1   | project1_07 | 12              | 6            | NaN            |
        | project1   | project1_08 | 12              | 12           | NaN            |
        | project2   | project2_09 | NaN             | NaN          | 21             |
        | project2   | project2_10 | NaN             | NaN          | 24             |
        | project2   | project2_11 | NaN             | NaN          | 27             |

        Now consider that we have the following project list data frame called
        project_list:

        Project ID | Project data file | Total project construction time months | ...
        -----------|-------------------|----------------------------------------|---
        project1   | project1_data     | 9                                      | ...
        project2   | project2_data     | 9                                      | ...
        project3   | project3_data     | 9                                      | ...

        OUTER join project_list with parametric_value_list such that you
        get the following data frame. The outer join ensures that even
        projects that do not have parametrics attached to them find
        their way to the list of projects to be executed.

        | Project ID | Serial      | alpha/fizz/buzz | beta/foo/bar | gamma/dogs/cats  Project data file | ...
        |------------|-------------|-----------------|--------------|----------------|-------------------| ...
        | project1   | project1_00 | 0               | 0            | NaN            | project1_data     | ...
        | project1   | project1_01 | 0               | 6            | NaN            | project1_data     | ...
        | project1   | project1_02 | 0               | 12           | NaN            | project1_data     | ...
        | project1   | project1_03 | 6               | 0            | NaN            | project1_data     | ...
        | project1   | project1_04 | 6               | 6            | NaN            | project1_data     | ...
        | project1   | project1_05 | 6               | 12           | NaN            | project1_data     | ...
        | project1   | project1_06 | 12              | 0            | NaN            | project1_data     | ...
        | project1   | project1_07 | 12              | 6            | NaN            | project1_data     | ...
        | project1   | project1_08 | 12              | 12           | NaN            | project1_data     | ...
        | project2   | project2_09 | NaN             | NaN          | 21             | project2_data     | ...
        | project2   | project2_10 | NaN             | NaN          | 24             | project2_data     | ...
        | project2   | project2_11 | NaN             | NaN          | 27             | project2_data     | ...
        | project3   | NaN         | NaN             | NaN          | NaN            | project3_data     | ...

        This data frame is in place to run with a modified project manager
        runner. The modification to the runner will run modifications to the
        project data dataframes before running them in a project. The columns
        that contain the modifications are the ones that contain the slashes.

        The outer join will ensure that all projects, including those that do
        not have parametric modification, are joined in. Further, the outer
        join will mean that there are no additional flags that can introduce
        errors in the project list.

        As before, NaN values are expected and signify that a particular
        parametric variable does not need to be modified for the project
        that is in the same row.

        Also, NaN in the Serial column means that a serial number will be
        added later because the project did not have any parametric modifications
        """
        result = project_list.merge(right=parametric_value_list, how='left', on='Project ID')
        return result

    def modify_project_data_dataframes(self, project_data_dataframes, project_parameters):
        """
        This method modifies project data dataframes according to the
        parametric modifications in the project parameters. It does not
        return a value because dataframes are modified in place.

        Note: This method will modify the dataframes in place. This isn't
        a problem if the dataframes are returned from
        XlsxReader.read_all_sheets_from_xlsx.

        If the dataframe name, column name or row name are not found, an
        XlsxOperationException is raised.

        Parameters
        ----------
        project_data_dataframes : dict
            Keys in this dictionary are the names of the sheets where
            the dataframes are parsed from. Values are the dataframes
            to be modified.

        project_parameters : pandas.Series
            The enhanced project parameters as created by
            create_parametric_value_list that have the values to
            place into the dataframes.

        Returns
        -------
        None
            Dataframes are modified in place.

        Raises
        ------
        XlsxOperationException
            This exception is raised of a dataframe, row or column
            is not found. The message is descriptive to help diagnose the
            problem during operation.
        """
        # This is a regex to match a column name that specifies a change to make
        # to a cell
        cell_spec_re = re.compile('^.*/.*/.*$')

        # Go through each project parameter
        for index, value in project_parameters.iteritems():

            # If the column specifies a cell to change in the dataframe
            if cell_spec_re.match(index) and not pd.isnull(value):
                dataframe_name, row_name, column_name = index.split('/')

                # Check if dataframe exists
                if dataframe_name not in project_data_dataframes:
                    raise XlsxOperationException(
                        f'Datframe {dataframe_name} not found. Please check the project_data spreadsheet and project_list.')

                df = project_data_dataframes[dataframe_name]
                first_col = df.columns[0]

                # Check if row exists
                if df.loc[df[first_col] == row_name].empty:
                    raise XlsxOperationException(
                        f'Row {row_name} not found in dataframe {dataframe_name}. Please check the project_data spreadsheet and project_list.')

                # Check if column exists
                if df.loc[df[first_col] == row_name, column_name].empty:
                    raise XlsxOperationException(
                        f'Column {column_name} not found in dataframe {dataframe_name}. Please check the project_data spreadsheet and project_list.')

                # If all the above check pass, check to make sure the value is not nan.
                # If it is not nan, then a modification needs to be made.
                if not np.isnan(value):
                    df.loc[df[first_col] == row_name, column_name] = value

    def create_master_input_dictionary(self, project_data_dataframes, project_parameters):
        """
        This method takes a dictionary of dataframes that are the project data
        and unites them with the project parameters as found in the project list
        sheet.

        Parameters
        ----------
        project_data_dataframes : dict
            This is a dictionary for the project data .xlsx file. The keys
            are names of sheets and the values are the dataframe contents of
            the sheets.

        project_parameters : pandas.Series
            Series representing the project data, which is the second set
            of data described in the XlsxReader class docstring. The caller
            of this function is responsible for parsing out the project
            data into a series from which these data can be extracted.
            See the subclasses of XlsxManagerRunner for examples on how this
            project series is read from a spreadsheet.

        Returns
        -------
        dict
            An master input dictionary suitable to pass to an instance
            of Manager to run all the cost module sin LandBOSSE.
        """
        # First, read all inputs that come from .csv or .xlsx files.
        # erection_input_worksheets come from the input data spreadsheet.
        # Their string values are the names of the sheets in the Excel
        # workbook and the keys in the erection_project_data_dict dictionary.

        # Incomplete project dict will hold the input dictionary
        # configurations.
        incomplete_input_dict = dict()

        # Read all project_data sheets.
        # The erection module takes in a bunch of keys and values under the
        # 'project_data' key in the incomplete_input_dict

        erection_input_worksheets = [
            'crane_specs',
            'equip',
            'crew',
            'equip_price',
            'crew_price',
            'material_price',
            'components'
        ]

        erection_project_data_dict = dict()
        for worksheet in erection_input_worksheets:
            erection_project_data_dict[worksheet] = project_data_dataframes[worksheet]

        # Add the erection project data to the incomplete_input_dict
        incomplete_input_dict['project_data'] = erection_project_data_dict

        # Get the first set of data
        incomplete_input_dict['rsmeans'] = project_data_dataframes['rsmeans']
        incomplete_input_dict['site_facility_building_area_df'] = project_data_dataframes['site_facility_building_area']
        incomplete_input_dict['material_price'] = project_data_dataframes['material_price']

        # The weather window is stored on a sheet of the project_data, but
        # needs preprocessing after it is read. The preprocessing changes it
        # from wind toolkit format to a dataframe.
        weather_window_input_df = project_data_dataframes['weather_window']
        incomplete_input_dict['weather_window'] = read_weather_window(weather_window_input_df)

        # Read development tab:
        # incomplete_input_dict['development_df'] = project_data.parse('development')
        incomplete_input_dict['development_df'] = project_data_dataframes['development']

        # FoundationCost needs to have all the component data split into separate
        # NumPy arrays.
        incomplete_input_dict['component_data'] = erection_project_data_dict['components']
        for component in incomplete_input_dict['component_data'].keys():
            incomplete_input_dict[component] = np.array(incomplete_input_dict['component_data'][component])

        incomplete_input_dict['cable_specs_pd'] = project_data_dataframes['cable_specs']

        # These columns come from the columns in the project definition .xlsx
        incomplete_input_dict['project_id'] = project_parameters['Project ID']
        incomplete_input_dict['num_turbines'] = project_parameters['Number of turbines']
        incomplete_input_dict['construct_duration'] = project_parameters['Total project construction time (months)']
        incomplete_input_dict['hub_height_meters'] = project_parameters['Hub height m']
        incomplete_input_dict['rotor_diameter_m'] = project_parameters['Rotor diameter m']
        incomplete_input_dict['wind_shear_exponent'] = project_parameters['Wind shear exponent']
        incomplete_input_dict['turbine_rating_MW'] = project_parameters['Turbine rating MW']
        incomplete_input_dict['breakpoint_between_base_and_topping_percent'] = \
            project_parameters['Breakpoint between base and topping (percent)']
        incomplete_input_dict['fuel_usd_per_gal'] = project_parameters['Fuel cost USD per gal']
        incomplete_input_dict['rate_of_deliveries'] = project_parameters['Rate of deliveries (turbines per week)']
        incomplete_input_dict['turbine_spacing_rotor_diameters'] = project_parameters['Turbine spacing (times rotor diameter)']
        incomplete_input_dict['depth'] = project_parameters['Foundation depth m']
        incomplete_input_dict['rated_thrust_N'] = project_parameters['Rated Thrust (N)']
        incomplete_input_dict['bearing_pressure_n_m2'] = project_parameters['Bearing Pressure (n/m2)']
        incomplete_input_dict['gust_velocity_m_per_s'] = project_parameters['50-year Gust Velocity (m/s)']
        incomplete_input_dict['project_size_megawatts'] = project_parameters['Number of turbines'] * project_parameters['Turbine rating MW']

        incomplete_input_dict['road_length_adder_m'] = project_parameters['Road length adder (m)']
        incomplete_input_dict['fraction_new_roads'] = project_parameters['Percent of roads that will be constructed']
        incomplete_input_dict['road_quality'] = project_parameters['Road Quality (0-1)']
        incomplete_input_dict['line_frequency_hz'] = project_parameters['Line Frequency (Hz)']
        incomplete_input_dict['plant_capacity_MW'] = project_parameters['Turbine rating MW'] * project_parameters['Number of turbines']
        incomplete_input_dict['row_spacing_rotor_diameters'] = project_parameters['Row spacing (times rotor diameter)']
        incomplete_input_dict['user_defined_distance_to_grid_connection'] = project_parameters['Flag for user-defined home run trench length (0 = no; 1 = yes)']
        incomplete_input_dict['distance_to_grid_connection_km'] = project_parameters['Combined Homerun Trench Length to Substation (km)']
        incomplete_input_dict['crew'] = incomplete_input_dict['project_data']['crew']
        incomplete_input_dict['crew_cost'] = incomplete_input_dict['project_data']['crew_price']

        #read in RSMeans per diem:
        crew_cost = incomplete_input_dict['project_data']['crew_price']
        crew_cost = crew_cost.set_index("Labor type ID", drop=False)
        incomplete_input_dict['rsmeans_per_diem'] = crew_cost.loc['RSMeans', 'Per diem USD per day']

        incomplete_input_dict['fuel_cost_usd_per_gal'] = project_parameters['Fuel cost USD per gal']

        incomplete_input_dict['line_frequency_hz'] = project_parameters['Line Frequency (Hz)']
        incomplete_input_dict['plant_capacity_MW'] = project_parameters['Turbine rating MW'] * project_parameters['Number of turbines']
        incomplete_input_dict['row_spacing_rotor_diameters'] = project_parameters['Row spacing (times rotor diameter)']
        incomplete_input_dict['user_defined_home_run_trench'] = project_parameters[
            'Flag for user-defined home run trench length (0 = no; 1 = yes)']
        incomplete_input_dict['trench_len_to_substation_km'] = project_parameters[
            'Combined Homerun Trench Length to Substation (km)']

        # Add inputs for transmission & Substation modules:
        incomplete_input_dict['distance_to_interconnect_mi'] = project_parameters['Distance to interconnect (miles)']
        incomplete_input_dict['interconnect_voltage_kV'] = project_parameters['Interconnect Voltage (kV)']
        new_switchyard = True
        if project_parameters['New Switchyard (y/n)'] == 'y':
            new_switchyard = True
        else:
            new_switchyard = False
        incomplete_input_dict['new_switchyard'] = new_switchyard

        incomplete_input_dict['critical_speed_non_erection_wind_delays_m_per_s'] = project_parameters['Non-Erection Wind Delay Critical Speed (m/s)']
        incomplete_input_dict['critical_height_non_erection_wind_delays_m'] = project_parameters['Non-Erection Wind Delay Critical Height (m)']

        incomplete_input_dict['road_width_ft'] = project_parameters['Road width (ft)']
        incomplete_input_dict['road_thickness'] = project_parameters['Road thickness (in)']
        incomplete_input_dict['crane_width'] = project_parameters['Crane width (m)']
        incomplete_input_dict['num_hwy_permits'] = project_parameters['Number of highway permits']
        incomplete_input_dict['num_access_roads'] = project_parameters['Number of access roads']
        incomplete_input_dict['overtime_multiplier'] = project_parameters['Overtime multiplier']
        incomplete_input_dict['allow_same_flag'] = True if project_parameters['Allow same flag'] == 'y' else False

        override_total_mgmt_cost_col_name = 'Override total management cost (0 does not override)'
        if override_total_mgmt_cost_col_name in project_parameters and project_parameters[override_total_mgmt_cost_col_name] > 0:
            incomplete_input_dict['override_total_management_cost'] = \
                project_parameters[override_total_mgmt_cost_col_name]
        else:
            incomplete_input_dict['markup_contingency'] = project_parameters['Markup contingency']
            incomplete_input_dict['markup_warranty_management'] = project_parameters['Markup warranty management']
            incomplete_input_dict['markup_sales_and_use_tax'] = project_parameters['Markup sales and use tax']
            incomplete_input_dict['markup_overhead'] = project_parameters['Markup overhead']
            incomplete_input_dict['markup_profit_margin'] = project_parameters['Markup profit margin']

        # Now fill any missing values with sensible defaults.
        defaults = DefaultMasterInputDict()
        master_input_dict = defaults.populate_input_dict(incomplete_input_dict=incomplete_input_dict)
        return master_input_dict

    def create_serial_number(self, project_id, index, max_index):
        """
        create_serial_number creates serial numbers left padded with
        zeros. By left padding the numbers, alphabetic sorts and numeric
        sorts create the same sequence. For example, in a sequence of
        100 total elements, 5 would be represented as "005"

        This left padded number is appended to the end of a string so
        you have something like "project_001"

        Parameters
        ----------
        project_id : str
            Base name of the project.

        index : int
            The index of the project in the sequence of projects

        max_index : int
            The total number of indices in the sequence.

        Returns
        -------
        str
            The left padded serial number as a string.
        """
        total_digit_count = 1
        index_digit_count = len(str(index))

        if 0 < max_index < 1e1 - 1:
            total_digit_count = 1
        elif 1e1 <= max_index < 1e2 - 1:
            total_digit_count = 2
        elif 1e2 <= max_index < 1e3 - 1:
            total_digit_count = 3
        elif 1e3 <= max_index < 1e4 - 1:
            total_digit_count = 4
        elif 1e4 <= max_index < 1e5 - 1:
            total_digit_count = 5
        elif 1e5 <= max_index < 1e6 - 1:
            total_digit_count = 6
        elif 1e6 <= max_index < 1e7 - 1:
            total_digit_count = 7
        elif 1e7 <= max_index < 1e8 - 1:
            total_digit_count = 8
        else:
            total_digit_count = 9

        padding = '0' * (total_digit_count - index_digit_count)
        return f'{project_id}_{padding}{index}'
