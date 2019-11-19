import pandas as pd
import numpy as np

class DefaultMasterInputDictSAM:
    """
       DefaultMasterInputDictSAM is a class that handles all the default values
       for the master input dictionary which will be exported to the System Advisor Model (SAM)
    """

    def __init__(self):
        """
            This constructor creates the defaults master input dictionary for SAM.
        """
        self.sam_defaults = dict()

        self.crane_specs_columns = ['Equipment name'          ,    'Crane name'          ,    'Boom system',  'Crane capacity tonne' , 'Speed of travel km per hr' , 'Hoist speed m per min' ,'Crew type ID', 'Equipment ID' , 'Setup time hr' , 'Max wind speed m per s' , 'Hub height m' , 'Max capacity tonne' , 'Radius m' , 'Hook Height m' , 'Mobilization cost USD']
        self.crane_specs_data = \
            [  #'Equipment name'       ,    'Crane name'      ,     'Boom system'               ,       'Crane capacity tonne'  ,   'Speed of travel km per hr' ,   'Hoist speed m per min' ,   'Crew type ID'  ,   'Equipment ID'  ,   'Setup time hr' ,   'Max wind speed m per s'    ,   'Hub height m'  ,   'Max capacity tonne'    ,   'Radius m'  ,   'Hook Height m' ,   'Mobilization cost USD'
                ['Offload crane'       ,    'LB 75'           ,     'Hydraulic'                 ,        75                     ,    40                         ,    60                    ,   'C0'            ,   'OL1'           ,    0              ,    10                         ,    12.5           ,    38                     ,    5.4        ,    12.5           ,    99 ],
                ['Offload crane'       ,    'LB 258'          ,     'Hydraulic'                 ,        200                    ,    40                         ,    60                    ,   'C0'            ,   'OL2'           ,    0              ,    10                         ,    48.0           ,    63                     ,    11.0       ,    48.0           ,    99 ],
                ['Crawler crane'       ,    'M999'            ,     '22EL'                      ,        275                    ,    2                          ,    20                    ,   'C1'            ,   'B1'            ,    0              ,    9                          ,    57.0           ,    67                     ,    14.0       ,    57.0           ,    99 ],
                ['Crawler crane'       ,    'LR1500'          ,     'SL3F'                      ,        500                    ,    2                          ,    20                    ,   'C1'            ,   'E1'            ,    0              ,    9                          ,    80.0           ,    102                    ,    16.0       ,    94.0           ,    99 ],
                ['Crawler crane'       ,    'LR1500'          ,     'SL3F'                      ,        500                    ,    2                          ,    20                    ,   'C1'            ,   'E1'            ,    0              ,    9                          ,    85.0           ,    95                     ,    16.0       ,    100.0          ,    99 ],
                ['Crawler crane'       ,    'LR1500'          ,     'SL3F'                      ,        500                    ,    2                          ,    20                    ,   'C1'            ,   'E1'            ,    0              ,    9                          ,    90.0           ,    87                     ,    16.0       ,    106.0          ,    99 ],
                ['Crawler crane'       ,    'LR1500'          ,     'SL3F'                      ,        500                    ,    2                          ,    20                    ,   'C1'            ,   'E1'            ,    0              ,    9                          ,    100.0          ,    77                     ,    18.0       ,    112.0          ,    99 ],
                ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,        500                    ,    2                          ,    20                    ,   'C1'            ,   'E1'            ,    2              ,    9                          ,    80.0           ,    112                    ,    16.0       ,    94.0           ,    99 ],
                ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,        500                    ,    2                          ,    20                    ,   'C1'            ,   'E1'            ,    2              ,    9                          ,    90.0           ,    105                    ,    16.0       ,    100.0          ,    99 ],
                ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,        500                    ,    2                          ,    20                    ,   'C1'            ,   'E1'            ,    2              ,    9                          ,    100.0          ,    90                     ,    16.0       ,    112.0          ,    99 ],
                ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,        500                    ,    2                          ,    20                    ,   'C1'            ,   'E1'            ,    2              ,    9                          ,    120.0          ,    74                     ,    18.0       ,    130.0          ,    99 ],
                ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,        500                    ,    2                          ,    20                    ,   'C1'            ,   'E1'            ,    2              ,    9                          ,    130.0          ,    60                     ,    20.0       ,    142.0          ,    99 ],
                ['Crawler crane'       ,    'LR1600/2'        ,     'SL8F3'                     ,        600                    ,    2                          ,    20                    ,   'C2'            ,   'E2'            ,    0              ,    9                          ,    80.0           ,    137                    ,    18.0       ,    93.0           ,    99 ],
                ['Crawler crane'       ,    'LR1600/2'        ,     'SL8F3'                     ,        600                    ,    2                          ,    20                    ,   'C2'            ,   'E2'            ,    0              ,    9                          ,    100.0          ,    118                    ,    18.0       ,    114.0          ,    99 ],
                ['Crawler crane'       ,    'LR1600/2'        ,     'SL3F'                      ,        600                    ,    2                          ,    20                    ,   'C2'            ,   'E2'            ,    0              ,    9                          ,    105.0          ,    93                     ,    18.0       ,    117.0          ,    99 ],
                ['Crawler crane'       ,    'LR1600/2'        ,     'HSL4DF + Derrick boom'     ,        600                    ,    2                          ,    20                    ,   'C2'            ,   'E2'            ,    2              ,    9                          ,    120.0          ,    87                     ,    20.0       ,    135.0          ,    99 ],
                ['Crawler crane'       ,    'LR1600/2'        ,     'SL13DFB + Derrick'         ,        600                    ,    2                          ,    20                    ,   'C2'            ,   'E2'            ,    2              ,    9                          ,    135.0          ,    96                     ,    20.0       ,    147.0          ,    99 ],
                ['Crawler crane'       ,    'LR1600/2'        ,     'SL13DFB + Derrick'         ,        600                    ,    2                          ,    20                    ,   'C2'            ,   'E2'            ,    2              ,    9                          ,    140.0          ,    87                     ,    24.0       ,    152.0          ,    99 ],
                ['Crawler crane'       ,    'LR1600/2'        ,     'SL13DFB2 + Derrick'        ,        600                    ,    2                          ,    20                    ,   'C2'            ,   'E2'            ,    2              ,    9                          ,    150.0          ,    71                     ,    24.0       ,    164.0          ,    99 ],
                ['Crawler crane'       ,    'LR1750/2'        ,     'HSL8HS'                    ,        750                    ,    2                          ,    20                    ,   'C3'            ,   'E3'            ,    0              ,    9                          ,    80.0           ,    111                    ,    18.0       ,    101.0          ,    99 ],
                ['Crawler crane'       ,    'LR1500/2'        ,     'HSL8HS'                    ,        750                    ,    2                          ,    20                    ,   'C3'            ,   'E3'            ,    0              ,    9                          ,    95.0           ,    110                    ,    18.0       ,    109.0          ,    99 ],
                ['Crawler crane'       ,    'LR1750/2'        ,     'HSL7DHS'                   ,        750                    ,    2                          ,    20                    ,   'C3'            ,   'E3'            ,    2              ,    9                          ,    120.0          ,    108                    ,    18.0       ,    136.0          ,    99 ],
                ['Crawler crane'       ,    'LR1750/2'        ,     'HSL7DHS'                   ,        750                    ,    2                          ,    20                    ,   'C3'            ,   'E3'            ,    2              ,    9                          ,    130.0          ,    98                     ,    18.0       ,    147.0          ,    99 ],
                ['Crawler crane'       ,    'LR1500/2'        ,     'HSL7DHS'                   ,        750                    ,    2                          ,    20                    ,   'C3'            ,   'E3'            ,    2              ,    9                          ,    140.0          ,    89                     ,    22.0       ,    152.0          ,    99 ],
                ['Crawler crane'       ,    'LR1750/2'        ,     'SX3D4F2B Derrick (walk)'   ,        750                    ,    2                          ,    20                    ,   'C3'            ,   'E3'            ,    0              ,    9                          ,    140.0          ,    141                    ,    28.0       ,    154.0          ,    99 ],
                ['Crawler crane'       ,    'LR1750/2'        ,     'SX3D4F2B Derrick (walk)'   ,        750                    ,    2                          ,    20                    ,   'C3'            ,   'E3'            ,    0              ,    9                          ,    150.0          ,    118                    ,    28.0       ,    165.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'SL3F'                      ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    3              ,    9                          ,    100.0          ,    179                    ,    18.0       ,    114.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'SL3F'                      ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    3              ,    9                          ,    110.0          ,    152                    ,    18.0       ,    120.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    3              ,    9                          ,    120.0          ,    179                    ,    20.0       ,    132.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    3              ,    9                          ,    140.0          ,    133                    ,    18.0       ,    136.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    3              ,    9                          ,    150.0          ,    154                    ,    18.0       ,    147.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    3              ,    9                          ,    155.0          ,    140                    ,    22.0       ,    152.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    3              ,    9                          ,    160.0          ,    120                    ,    26.0       ,    174.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    3              ,    9                          ,    180.0          ,    73                     ,    22.0       ,    192.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    3              ,    9                          ,    185.0          ,    54                     ,    34.0       ,    198.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'PDW3B Derrick'             ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    6              ,    9                          ,    130.0          ,    227                    ,    28.0       ,    147.0          ,    99 ],
                ['Crawler crane'       ,    'LR11000'         ,     'PDW3B2 Derrick'            ,        1000                   ,    1                          ,    25                    ,   'C4'            ,   'E4'            ,    6              ,    9                          ,    165.0          ,    142                    ,    26.0       ,    174.0          ,    99 ]
            ]
        self.crane_specs = pd.DataFrame(self.crane_specs_data, columns=self.crane_specs_columns)
        self.sam_defaults['crane_specs'] = self.crane_specs

        self.equip_columns =  ['Equipment ID'    ,   'Operation'  ,     'Equipment name'   ,   'Crane capacity tonne'  ,      'Number of equipment']
        self.equip_data = [ # Equipment ID    ,   Operation       Equipment name      Crane capacity tonne        Number of equipment
                    ['E1'           ,   'Base'      ,   'Crawler crane'     , 500                   ,    1 ],
                    ['E1'           ,   'Base'      ,   'Truck crane'       , 50                    ,    1 ],
                    ['E1'           ,   'Top'       ,   'Crawler crane'     , 500                   ,    1 ],
                    ['E1'           ,   'Top'       ,   'Truck crane'       , 50                    ,    2 ],
                    ['E2'           ,   'Top'       ,   'Crawler crane'     , 600                   ,    1 ],
                    ['E2'           ,   'Top'       ,   'Truck crane'       , 50                    ,    2 ],
                    ['E2'           ,   'Top'       ,   'RT'                , 100                   ,    2 ],
                    ['E3'           ,   'Top'       ,   'Crawler crane'     , 750                   ,    1 ],
                    ['E3'           ,   'Top'       ,   'RT'                , 100                   ,    2 ],
                    ['E4'           ,   'Top'       ,   'Crawler crane'     , 1000                  ,    1 ],
                    ['E4'           ,   'Top'       ,   'RT'                , 100                   ,    2 ],
                    ['ST1'          ,   'Top'       ,   'Mobile crane'      , 200                   ,    1 ],
                    ['ST1'          ,   'Top'       ,   'RT'                , 100                   ,    2 ],
                    ['OL1'          ,   'Offload'   ,   'Offload crane'     , 75                    ,    2 ],
                    ['OL2'          ,   'Offload'   ,   'Offload crane'     , 200                   ,    2 ],
                    ['B1'           ,   'Base'      ,   'Crawler crane'     , 275                   ,    1 ],
                    ['B1'           ,   'Base'      ,   'Truck crane'       , 50                    ,    1 ],
                    ['E2'           ,   'Base'      ,   'Crawler crane'     , 600                   ,    1 ],
                    ['E2'           ,   'Base'      ,   'Truck crane'       , 50                    ,    2 ],
                    ['E2'           ,   'Base'      ,   'RT'                , 100                   ,    2 ],
                    ['E3'           ,   'Base'      ,   'Crawler crane'     , 750                   ,    1 ],
                    ['E3'           ,   'Base'      ,   'RT'                , 100                   ,    2 ],
                    ['E4'           ,   'Base'      ,   'Crawler crane'     , 1000                  ,    1 ],
                    ['E4'           ,   'Base'      ,   'RT'                , 100                   ,    2 ],
                    ['ST1'          ,   'Base'      ,   'Mobile crane'      , 200                   ,    1 ],
                    ['ST1'          ,   'Base'      ,   'RT'                , 100                   ,    2 ],
                    ['OL2'          ,   'Base'      ,   'Offload crane'     , 200                   ,    2 ]
                  ]
        self.equip = pd.DataFrame(self.equip_data, columns=self.equip_columns)
        self.sam_defaults['equip'] = self.equip

        self.equip_price_columns = ['Equipment name',  'Crane capacity tonne',  'Equipment price USD per hour',  'Cost USD per breakdown',  'Fuel consumption gal per day']
        self.equip_price_data = [# Equipment name        Crane capacity tonne        Equipment price USD per hour        Cost USD per breakdown      Fuel consumption gal per day
                                ['Mobile crane'     ,    75                     ,    99                          ,   np.nan                   ,    99.0 ],
                                ['Mobile crane'     ,    200                    ,    99                          ,   np.nan                   ,    99.0 ],
                                ['Crawler crane'    ,    275                    ,    99                          ,    99.0                    ,    99.0 ],
                                ['Crawler crane'    ,    250                    ,    99                          ,    99.0                    ,    99.0 ],
                                ['Crawler crane'    ,    400                    ,    99                          ,    99.0                    ,    99.0 ],
                                ['Crawler crane'    ,    500                    ,    99                          ,    99.0                    ,    99.0 ],
                                ['Crawler crane'    ,    600                    ,    99                          ,    99.0                    ,    99.0 ],
                                ['Crawler crane'    ,    750                    ,    99                          ,    99.0                    ,    99.0 ],
                                ['Crawler crane'    ,    1000                   ,    99                          ,    99.0                    ,    99.0 ],
                                ['Crawler crane'    ,    1350                   ,    99                          ,    99.0                    ,    99.0 ],
                                ['Truck crane'      ,    50                     ,    99                          ,   np.nan                   ,   np.nan],
                                ['RT'               ,    100                    ,    99                          ,   np.nan                   ,   np.nan],
                                ['Offload crane'    ,    75                     ,    99                          ,   np.nan                   ,    99.0 ],
                                ['Offload crane'    ,    200                    ,    99                          ,   np.nan                   ,    99.0 ]
                            ]
        self.equip_price = pd.DataFrame(self.equip_price_data, columns=self.equip_price_columns)
        self.sam_defaults['equip_price'] = self.equip_price

        self.crew_price_columns = ['Labor type ID' , 'Hourly rate USD per hour' , 'Per diem USD per day']
        self.crew_price_data = [ # Labor type ID'        ,   Hourly rate USD per hour    ,   Per diem USD per day
                            ['Crane operator'       ,    99.0                        ,    99 ],
                            ['Oiler'                ,    99.0                        ,    99 ],
                            ['Rigger'               ,    99.0                        ,    99 ],
                            ['Truck driver'         ,    99.0                        ,    99 ],
                            ['Iron worker'          ,    99.0                        ,    99 ],
                            ['Project manager'      ,    99.0                        ,    99 ],
                            ['Site manager'         ,    99.0                        ,    99 ],
                            ['Construction manager' ,    99.0                        ,    99 ],
                            ['Project engineer'     ,    99.0                        ,    99 ],
                            ['Safety or qc manager' ,    99.0                        ,    99 ],
                            ['Logistics manager'    ,    99.0                        ,    99 ],
                            ['Rigger foreman'       ,    99.0                        ,    99 ],
                            ['Rigger'               ,    99.0                        ,    99 ],
                            ['Operator'             ,    99.0                        ,    99 ],
                            ['Oiler'                ,    99.0                        ,    99 ],
                            ['Electrician'          ,    99.0                        ,    99 ],
                            ['Tool room'            ,    99.0                        ,    99 ],
                            ['QC/QA tech'           ,    99.0                        ,    99 ],
                            ['Office admin'         ,    99.0                        ,    99 ],
                            ['RSMeans'              ,   np.nan                       ,    99 ]]

        self.crew_price = pd.DataFrame(self.crew_price_data, columns=self.crew_price_columns)
        self.sam_defaults['crew_price'] = self.crew_price

        self.crew_cost_columns = ['Labor type ID' , 'Hourly rate USD per hour' , 'Per diem USD per day']
        self.crew_cost_data = [ #  Labor type ID'        ,   Hourly rate USD per hour    ,   Per diem USD per day
                                    ['Crane operator'       ,    99.0                       ,    99 ],
                                    ['Oiler'                ,    99.0                       ,    99 ],
                                    ['Rigger'               ,    99.0                       ,    99 ],
                                    ['Truck driver'         ,    99.0                       ,    99 ],
                                    ['Iron worker'          ,    99.0                       ,    99 ],
                                    ['Project manager'      ,    99.0                       ,    99 ],
                                    ['Site manager'         ,    99.0                       ,    99 ],
                                    ['Construction manager' ,    99.0                       ,    99 ],
                                    ['Project engineer'     ,    99.0                       ,    99 ],
                                    ['Safety or qc manager' ,    99.0                       ,    99 ],
                                    ['Logistics manager'    ,    99.0                       ,    99 ],
                                    ['Rigger foreman'       ,    99.0                       ,    99 ],
                                    ['Rigger'               ,    99.0                       ,    99 ],
                                    ['Operator'             ,    99.0                       ,    99 ],
                                    ['Oiler'                ,    99.0                       ,    99 ],
                                    ['Electrician'          ,    99.0                       ,    99 ],
                                    ['Tool room'            ,    99.0                       ,    99 ],
                                    ['QC/QA tech'           ,    99.0                       ,    99 ],
                                    ['Office admin'         ,    99.0                       ,    99 ],
                                    ['RSMeans'              ,   np.nan                      ,    99 ]]

        self.crew_cost = pd.DataFrame(self.crew_cost_data, columns=self.crew_cost_columns)
        self.sam_defaults['crew_cost'] = self.crew_cost



        self.crew_columns = ['Crew type ID',	'Operation',	'Crew name',	'Labor type ID',	'Number of workers']
        self.crew_data = [#      'Crew type ID'  ,	'Operation'                 ,	'Crew name'                                     ,      'Labor type ID'      ,	'Number of workers'
                            ['M0'           ,	'Management'	            ,   'Management - project size'	                    ,   'Project manager'       ,    1 ],
                            ['M0'           ,	'Management'	            ,   'Management - project size'	                    ,   'Site manager'	        ,    1 ],
                            ['M0'           ,	'Management'	            ,   'Management - project size'	                    ,   'Construction manager'	,    1 ],
                            ['M0'           ,	'Management'	            ,   'Management - project size'	                    ,   'Project engineer'	    ,    1 ],
                            ['M0'           ,	'Management'	            ,   'Management - project size'	                    ,   'Safety or qc manager'	,    1 ],
                            ['M0'           ,	'Management'	            ,   'Management - project size'	                    ,   'Logistics manager'	    ,    1 ],
                            ['M0'           ,	'Management'	            ,   'Management - project size'	                    ,   'Office admin'	        ,    1 ],
                            ['M1'           ,	'Management'	            ,   'Management - rate construction'                ,   'Tool room'	            ,    1 ],
                            ['M1'           ,	'Management'	            ,   'Management - rate construction'                ,	'Electrician'    	    ,    2 ],
                            ['MC0'          ,	'Mechanical completion'     ,   'Mechanical completion'                         ,	'QC/QA tech'	        ,    2 ],
                            ['MC0'          ,	'Mechanical completion'     ,   'Mechanical completion'                         ,	'Electrician'	        ,    1 ],
                            ['C0'           ,	'Offload'                   ,	'Offload can tower'	                            ,   'Crane operator'	    ,    2 ],
                            ['C0'           ,	'Offload'                   ,	'Offload can tower'	                            ,   'Oiler'	                ,    2 ],
                            ['C0'           ,	'Offload'                   ,	'Offload can tower'	                            ,   'Iron worker'	        ,    3 ],
                            ['C0'           ,	'Offload'                   ,	'Offload can tower'	                            ,   'Rigger foreman'	    ,    1 ],
                            ['C5'           ,	'Base'                      ,	'Base 300t'                                     ,	'Crane operator'	    ,    2 ],
                            ['C5'           ,	'Base'                      ,	'Base 300t'                                     ,	'Oiler'	                ,    2 ],
                            ['C5'           ,	'Base'                      ,	'Base 300t'                                     ,	'Iron worker'	        ,    3 ],
                            ['C5'           ,	'Base'                      ,	'Base 300t'                                     ,	'Truck driver'	        ,    1 ],
                            ['C5'           ,	'Base'                      ,	'Base 300t'                                     ,	'Rigger foreman'	    ,    1 ],
                            ['C5'           ,	'Base'                      ,	'Base 400t'                                     ,	'Crane operator'	    ,    2 ],
                            ['C5'           ,	'Base'                      ,	'Base 400t'                                     ,	'Oiler'	                ,    2 ],
                            ['C5'           ,	'Base'                      ,	'Base 400t'                                     ,	'Iron worker'	        ,    3 ],
                            ['C5'           ,	'Base'                      ,	'Base 400t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C5'           ,	'Base'                      ,	'Base 400t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C1'           ,	'Base'                      ,	'Base 500t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C1'           ,	'Base'                      ,	'Base 500t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C1'           ,	'Base'                      ,	'Base 500t'	                                    ,   'Iron worker'	        ,    3 ],
                            ['C1'           ,	'Base'                      ,	'Base 500t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C1'           ,	'Base'                      ,	'Base 500t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C6'           ,	'Top'                       ,	'Top 400t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C6'           ,	'Top'                       ,	'Top 400t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C6'           ,	'Top'                       ,	'Top 400t'	                                    ,   'Iron worker'	        ,    6 ],
                            ['C6'           ,	'Top'                       ,	'Top 400t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C6'           ,	'Top'                       ,	'Top 400t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C1'           ,	'Top'                       ,	'Top 500t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C1'           ,	'Top'                       ,	'Top 500t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C1'           ,	'Top'                       ,	'Top 500t'	                                    ,   'Iron worker'	        ,    6 ],
                            ['C1'           ,	'Top'                       ,	'Top 500t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C1'           ,	'Top'                       ,	'Top 500t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C2'           ,	'Top'                       ,	'Top 600t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C2'           ,	'Top'                       ,	'Top 600t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C2'           ,	'Top'                       ,	'Top 600t'	                                    ,   'Iron worker'	        ,    6 ],
                            ['C2'           ,	'Top'                       ,	'Top 600t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C2'           ,	'Top'                       ,	'Top 600t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C3'           ,	'Top'                       ,	'Top 750t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C3'           ,	'Top'                       ,	'Top 750t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C3'           ,	'Top'                       ,	'Top 750t'	                                    ,   'Iron worker'	        ,    6 ],
                            ['C3'           ,	'Top'                       ,	'Top 750t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C3'           ,	'Top'                       ,	'Top 750t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C4'           ,	'Top'                       ,	'Top 1000t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C4'           ,	'Top'                       ,	'Top 1000t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C4'           ,	'Top'                       ,	'Top 1000t'	                                    ,   'Iron worker'	        ,    6 ],
                            ['C4'           ,	'Top'                       ,	'Top 1000t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C4'           ,	'Top'                       ,	'Top 1000t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C1'           ,	'Base'                      ,	'Top 500t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C1'           ,	'Base'                      ,	'Top 500t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C1'           ,	'Base'                      ,	'Top 500t'	                                    ,   'Iron worker'	        ,    6 ],
                            ['C1'           ,	'Base'                      ,	'Top 500t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C1'           ,	'Base'                      ,	'Top 500t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C2'           ,	'Base'                      ,	'Top 600t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C2'           ,	'Base'                      ,	'Top 600t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C2'           ,	'Base'                      ,	'Top 600t'	                                    ,   'Iron worker'	        ,    6 ],
                            ['C2'           ,	'Base'                      ,	'Top 600t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C2'           ,	'Base'                      ,	'Top 600t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C3'           ,	'Base'                      ,	'Top 750t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C3'           ,	'Base'                      ,	'Top 750t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C3'           ,	'Base'                      ,	'Top 750t'	                                    ,   'Iron worker'	        ,    6 ],
                            ['C3'           ,	'Base'                      ,	'Top 750t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C3'           ,	'Base'                      ,	'Top 750t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C4'           ,	'Base'                      ,	'Top 1000t'	                                    ,   'Crane operator'	    ,    2 ],
                            ['C4'           ,	'Base'                      ,	'Top 1000t'	                                    ,   'Oiler'	                ,    2 ],
                            ['C4'           ,	'Base'                      ,	'Top 1000t'	                                    ,   'Iron worker'	        ,    6 ],
                            ['C4'           ,	'Base'                      ,	'Top 1000t'	                                    ,   'Truck driver'	        ,    1 ],
                            ['C4'           ,	'Base'                      ,	'Top 1000t'	                                    ,   'Rigger foreman'	    ,    1 ],
                            ['C0'           ,	'Base'                      ,	'Offload can tower'	                            ,   'Crane operator'	    ,    2 ],
                            ['C0'           ,	'Base'                      ,	'Offload can tower'	                            ,   'Oiler'	                ,    2 ],
                            ['C0'           ,	'Base'                      ,	'Offload can tower'	                            ,   'Iron worker'	        ,    3 ],
                            ['C0'           ,	'Base'                      ,	'Offload can tower'	                            ,   'Rigger foreman'        ,    1 ]]

        self.crew = pd.DataFrame(self.crew_data, columns=self.crew_columns)
        self.sam_defaults['crew'] = self.crew


        self.material_price_columns = ['Material type ID',  'Material price USD per unit' , 'Unit'  ,'Notes']
        self.material_price_data =[# 'Material type ID',                         'Material price USD per unit'           'Unit'                          ,   'Notes'
                                ['unique identifier for the material'   ,   'price of material per unit'        ,   'unit of measure used for cost' ,   np.nan],
                                ['Concrete 3000 psi'                    ,    99                                 ,   'cubic yard'                    ,   np.nan],
                                ['Concrete 5000 psi'                    ,    99                                 ,   'cubic yard'                    ,   np.nan],
                                ['Concrete 8000 psi'                    ,    99                                 ,   'cubic yard'                    ,   np.nan],
                                ['Steel - rebar'                        ,    99                                 ,   'ton (short)'                   ,   np.nan],
                                ['Road base - 3/4 inch crushed stone'   ,    99                                 ,   'Loose cubic yard'              ,   np.nan],
                                ['Excavated dirt'                       ,    0                                  ,   'cubic yard'                    ,   np.nan],
                                ['Backfill'                             ,    0                                  ,   'cubic yard'                    ,   np.nan]]

        self.material_price = pd.DataFrame(self.material_price_data, columns=self.material_price_columns)
        self.sam_defaults['material_price'] = self.material_price


        self.components_columns = ['Component', 'Mass tonne', 'Lift height m', 'Surface area sq m', 'Coeff drag', 'Coeff drag (installed)', 'Section height m', 'Lever arm m', 'Cycle time installation hrs', 'Offload hook height m', 'Offload cycle time hrs', 'Multplier drag rotor', 'Multiplier tower drag', 'Operation']
        self.components_data = [#  Component                ,   Mass tonne  ,    Lift height m   ,   Surface area sq m  ,   Coeff drag  ,   Coeff drag (installed)  ,   Section height m    ,   Lever arm m     ,   Cycle time installation hrs ,   Offload hook height m   ,   Offload cycle time hrs  ,   Multplier drag rotor    ,   Multiplier tower drag Operation
                                ['IEA 3.6-130 Bedplate'    ,    80          ,    82              ,    32.00             ,    0.7        ,    0.7                    ,    0                  ,    85.0           ,    2                          ,    6                      ,    0.5                    ,    1.000000               ,    0                      ,    'Top'],
                                ['IEA 3.6-130 Drivetrain'  ,    80          ,    86              ,    20.00             ,    0.9        ,    0.9                    ,    0                  ,    85.0           ,    2                          ,    6                      ,    0.5                    ,    0.000000               ,    0                      ,    'Top'],
                                ['Hub'                     ,    35          ,    85              ,    12.16             ,    1.1        ,    1.1                    ,    0                  ,    85.0           ,    1                          ,    6                      ,    0.5                    ,    0.000000               ,    0                      ,    'Top'],
                                ['Blade 1'                 ,    17          ,    85              ,    68.80             ,    0.1        ,    1.4                    ,    0                  ,    85.0           ,    1                          ,    6                      ,    0.5                    ,    0.666667               ,    0                      ,    'Top'],
                                ['Blade 2'                 ,    17          ,    85              ,    68.80             ,    0.1        ,    1.4                    ,    0                  ,    85.0           ,    1                          ,    6                      ,    0.5                    ,    0.666667               ,    0                      ,    'Top'],
                                ['Blade 3'                 ,    17          ,    85              ,    68.80             ,    0.1        ,    1.4                    ,    0                  ,    85.0           ,    1                          ,    6                      ,    0.5                    ,    0.666667               ,    0                      ,    'Top'],
                                ['Tower section 1'         ,    65          ,    20              ,    85.00             ,    0.6        ,    1.1                    ,    20                 ,    10.0           ,    1                          ,    6                      ,    0.5                    ,    0.000000               ,    1                      ,   'Base'],
                                ['Tower section 2'         ,    55          ,    40              ,    85.00             ,    0.6        ,    1.1                    ,    20                 ,    30.0           ,    1                          ,    6                      ,    0.5                    ,    0.000000               ,    1                      ,   'Base'],
                                ['Tower section 3'         ,    45          ,    60              ,    85.00             ,    0.6        ,    1.1                    ,    20                 ,    50.0           ,    1                          ,    6                      ,    0.5                    ,    0.000000               ,    1                      ,   'Base'],
                                ['Tower section 4'         ,    40          ,    85              ,    90.00             ,    0.6        ,    1.1                    ,    25                 ,    72.5           ,    1                          ,    6                      ,    0.5                    ,    0.000000               ,    1                      ,    'Top']]

        self.components = pd.DataFrame(self.components_data, columns=self.components_columns)
        self.sam_defaults['components'] = self.components
        self.sam_defaults['component_data'] = self.components


        self.rsmeans_columns = ['Operation ID', 'Type of cost', 'Material type ID', 'Rate USD per unit', 'Units', 'Daily output', 'Per Diem Hours (per unit)', 'Module', 'Number of workers', 'Notes']
        self.rsmeans_data = [
                                #Operation ID                                       ,   Type of cost        ,       Material type ID                            , Rate USD per unit ,   Units                           ,   Daily output                 ,   Per Diem Hours (per unit)    ,   Module          ,   Number of workers   ,   Notes
                                ['Concrete placement'                               ,   'Equipment rental'  ,       'Concrete 5000 psi'                         ,   99.0            ,   '$/cubic yard'                  ,   np.nan                       ,   np.nan                       ,   'Foundations'   ,   np.nan               ,   np.nan],
                                ['Rebar installation'                               ,   'Equipment rental'  ,       'Steel - rebar'                             ,   99.0            ,   '$/ton (short)'                 ,   np.nan                       ,   np.nan                       ,   'Foundations'   ,   np.nan               ,   np.nan],
                                ['Survey'                                           ,   'Equipment rental'  ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Clear and grub'                                   ,   'Equipment rental'  ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Topsoil stripping and stockpiling'                ,   'Equipment rental'  ,       np.nan                                      ,   99.0            ,   'cubic yard'                    ,   np.nan                       ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Stormwater pollution prevention'                  ,   'Equipment rental'  ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Culverts'                                         ,   'Equipment rental'  ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Compaction of soil (subgrade and crane path)'     ,   'Equipment rental'  ,       np.nan                                      ,   99.0            ,   'embankment cubic yards crane'  ,   np.nan                       ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Mass material movement (cut and fill)'            ,   'Equipment rental'  ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Placing road base (hauling)'                      ,   'Equipment rental'  ,       'Road base - 3/4 inch crushed stone'        ,   99.0            ,   'loose cubic yard'              ,   np.nan                       ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Rough grading road base'                          ,   'Equipment rental'  ,       np.nan                                      ,   99.0            ,   'Each (100000 square feet)'     ,   np.nan                       ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Compacting road base'                             ,   'Equipment rental'  ,       np.nan                                      ,   99.0            ,   'embankment cubic yards road'   ,   np.nan                       ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Final grading'                                    ,   'Equipment rental'  ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Road maintanp.nance'                              ,   'Equipment rental'  ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Decompaction of crane paths'                      ,   'Equipment rental'  ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Reseeding, planting, etc'                         ,   'Equipment rental'  ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Concrete placement'                               ,   'Labor'             ,       'Concrete 5000 psi'                         ,   99.0            ,   '$/cubic yard'                  ,   99.0                         ,   np.nan                       ,   'Foundations'   ,   99.0                 ,   np.nan],
                                ['Rebar installation'                               ,   'Labor'             ,       'Steel - rebar'                             ,   99.0            ,   '$/ton (short)'                 ,   99.0                         ,   np.nan                       ,   'Foundations'   ,   99.0                 ,   np.nan],
                                ['Survey'                                           ,   'Labor'             ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Clear and grub'                                   ,   'Labor'             ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Topsoil stripping and stockpiling'                ,   'Labor'             ,       np.nan                                      ,   99.0            ,   'cubic yard'                    ,   99.0                         ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Stormwater pollution prevention'                  ,   'Labor'             ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Culverts'                                         ,   'Labor'             ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Compaction of soil (subgrade and crane path)'     ,   'Labor'             ,       np.nan                                      ,   99.0            ,   'embankment cubic yards crane'  ,   99.0                         ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Mass material movement (cut and fill)'            ,   'Labor'             ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Placing road base (hauling)'                      ,   'Labor'             ,       'Road base - 3/4 inch crushed stone'        ,   99.0            ,   'loose cubic yard'              ,   99.0                         ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Rough grading road base'                          ,   'Labor'             ,       np.nan                                      ,   99.0            ,   'Each (100000 square feet)'     ,   99.0                         ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Compacting road base'                             ,   'Labor'             ,       np.nan                                      ,   99.0            ,   'embankment cubic yards road'   ,   99.0                         ,   99.0                         ,   'Roads'         ,   99.0                 ,   np.nan],
                                ['Final grading'                                    ,   'Labor'             ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Road maintanp.nance'                              ,   'Labor'             ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Decompaction of crane paths'                      ,   'Labor'             ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Reseeding, planting, etc'                         ,   'Labor'             ,       np.nan                                      ,   np.nan          ,   np.nan                          ,   np.nan                       ,   np.nan                       ,   'Roads'         ,   np.nan               ,   np.nan],
                                ['Excavation'                                       ,   'Equipment rental'  ,       'Excavated dirt'                            ,   99.0            ,   '$/cubic yard'                  ,   np.nan                       ,   np.nan                       ,   'Foundations'   ,   np.nan               ,   np.nan],
                                ['Excavation'                                       ,   'Labor'             ,       'Excavated dirt'                            ,   99.0            ,   '$/cubic yard'                  ,   99.0                         ,   99.0                         ,   'Foundations'   ,   99.0                 ,   np.nan],
                                ['Backfill'                                         ,   'Equipment rental'  ,       'Backfill'                                  ,   99.0            ,   '$/cubic yard'                  ,   np.nan                       ,   np.nan                       ,   'Foundations'   ,   np.nan               ,   np.nan],
                                ['Backfill'                                         ,   'Labor'             ,       'Backfill'                                  ,   99.0            ,   '$/cubic yard'                  ,   99.0                         ,   99.0                         ,   'Foundations'   ,   99.0                 ,   np.nan],
                                ['Collection'                                       ,   'Labor'             ,       np.nan                                      ,   99.0            ,   '$/hr'                          ,   99.0                         ,   99.0                         ,   'Collection'    ,   99.0                 ,   np.nan],
                                ['Collection'                                       ,   'Equipment'         ,       np.nan                                      ,   99.0            ,   '$/hr'                          ,   99.0                         ,   99.0                         ,   'Collection'    ,   np.nan               ,   np.nan],
                                ['Collection'                                       ,   'Labor'             ,       'dozer operator and .5 laborer cable reels' ,   99.0            ,   '$/hr'                          ,   np.nan                       ,   99.0                         ,   'Collection'    ,   99.0                 ,   np.nan],
                                ['Collection'                                       ,   'Equipment'         ,       '200 hp dozer cable reels'                  ,   99.0            ,   '$/hr'                          ,   np.nan                       ,   99.0                         ,   'Collection'    ,   np.nan               ,   np.nan],
                                ['Collection'                                       ,   'Labor'             ,       'Forklift Operator'                         ,   99.0            ,   '$/hr'                          ,   np.nan                       ,   99.0                         ,   'Collection'    ,   99.0                 ,   np.nan],
                                ['Collection'                                       ,   'Equipment'         ,       'all terrain fork lift for reel changes'    ,   99.0            ,   '$/hr'                          ,   np.nan                       ,   99.0                         ,   'Collection'    ,   np.nan               ,   np.nan]]

        self.rsmeans = pd.DataFrame(self.rsmeans_data, columns=self.rsmeans_columns)
        self.sam_defaults['rsmeans'] = self.rsmeans


        self.site_facility_building_area_df_columns = ['Size Min (MW)' , 'Size Max (MW)'   ,   'Building area (sq. ft.)']
        self.site_facility_building_area_df_data = [
                                                #   Size Min (MW)  , Size Max (MW)   ,   Building area (sq. ft.)
                                                    [ 0            ,  200            ,    3000 ],
                                                    [ 200          ,  500            ,    5000 ],
                                                    [ 500          ,  800            ,    7000 ],
                                                    [ 800          ,  1000           ,    9000 ],
                                                    [ 1000         ,  5000           ,    12000 ]]
        self.site_facility_building_area_df = pd.DataFrame(self.site_facility_building_area_df_data, columns=self.site_facility_building_area_df_columns)
        self.sam_defaults['site_facility_building_area_df'] = self.site_facility_building_area_df


        self.development_df_columns = ['Type of cost'  	 ,	'Cost USD'	, 	 'Phase of construction']
        self.development_df_data = [
                            #   'Type of cost'  	,   'Cost USD'	,     'Phase of construction'
                                ['Equipment rental' ,   0 		    ,     'Development'],
                                ['Labor'            ,   99          ,     'Development'],
                                ['Materials'        ,   0           ,     'Development'],
                                ['Mobilization'     ,   0           ,     'Development'],
                                ['Other'            ,   0           ,     'Development']]

        self.development_df = pd.DataFrame(self.development_df_data, columns=self.development_df_columns)
        self.sam_defaults['development_df'] = self.development_df

        self.cable_specs_columns = ['Array Cable'	,   'Conductor Size (mm2)'    ,	'Current Capacity (A)'    ,   'Rated Voltage (V)'   ,	'AC Resistance (Ohms/km)' ,       'Inductance (mH/km)'  ,   'Capacitance (nF/km)' ,   'Cost (USD/LF)']
        self.cable_specs_data = [#  Array Cable	,   Conductor Size (mm2)    ,	Current Capacity (A)    ,   Rated Voltage (V)   ,	AC Resistance (Ohms/km) ,       Inductance (mH/km)  ,   Capacitance (nF/km) ,   Cost (USD/LF)
                                    ['AWG 1/0'  ,	 120 	                ,    300 	                ,    36                 ,	 0.253                  ,	     0.398              ,	 0.179              ,	 99 ],
                                    ['AWG 4/0'  ,	 240 	                ,    440 	                ,    36                 ,	 0.125                  ,	     0.359              ,	 0.223              ,	 99 ],
                                    ['MCM 500'  ,	 500 	                ,    640 	                ,    36                 ,	 0.061                  ,	     0.317              ,	 0.293              ,	 99 ],
                                    ['MCM1000'  ,	 800 	                ,    830 	                ,    36                 ,	 0.037                  ,	     0.291              ,	 0.375              ,	 99 ],
                                    ['MCM1250'  ,	 1000 	                ,    935 	                ,    36                 ,	 0.029                  ,	     0.284              ,	 0.411              ,	 99 ]]
        self.cable_specs = pd.DataFrame(self.cable_specs_data, columns=self.cable_specs_columns)
        self.sam_defaults['cable_specs'] = self.cable_specs
        self.sam_defaults['cable_specs_pd'] = self.cable_specs

        self.sam_defaults['Multiplier tower drag'] = self.sam_defaults['components']['Multiplier tower drag'].to_numpy().astype('int64')
        self.sam_defaults['Multplier drag rotor'] = self.sam_defaults['components']['Multplier drag rotor'].to_numpy().astype('float64')
        self.sam_defaults['Lift height m'] = self.sam_defaults['components']['Lift height m'].to_numpy().astype('int64')
        self.sam_defaults['Coeff drag'] = self.sam_defaults['components']['Coeff drag'].to_numpy().astype('float64')
        self.sam_defaults['Coeff drag (installed)'] = self.sam_defaults['components']['Coeff drag (installed)'].to_numpy().astype('float64')
        self.sam_defaults['Offload hook height m'] = self.sam_defaults['components']['Offload hook height m'].to_numpy().astype('int64')
        self.sam_defaults['Section height m'] = self.sam_defaults['components']['Section height m'].to_numpy().astype('int64')
        # astype_inplace(self.sam_defaults['Section height m'], 'int64')
        self.sam_defaults['Mass tonne'] = self.sam_defaults['components']['Mass tonne'].to_numpy().astype('int64')
        self.sam_defaults['Surface area sq m'] = self.sam_defaults['components']['Surface area sq m'].to_numpy().astype('float64')
        self.sam_defaults['Offload cycle time hrs'] = self.sam_defaults['components']['Offload cycle time hrs'].to_numpy().astype('float64')
        self.sam_defaults['Lever arm m'] = self.sam_defaults['components']['Lever arm m'].to_numpy().astype('float64')
        self.sam_defaults['Component'] = self.sam_defaults['components']['Component'].to_numpy()
        self.sam_defaults['Cycle time installation hrs'] = self.sam_defaults['components']['Cycle time installation hrs'].to_numpy().astype('int64')


        self.sam_defaults['project_id']= 'project_1'
        self.sam_defaults['num_turbines']= 100
        self.sam_defaults['construct_duration']= 9
        self.sam_defaults['hub_height_meters']= 80
        self.sam_defaults['rotor_diameter_m']= 77
        self.sam_defaults['wind_shear_exponent']= 0.2
        self.sam_defaults['turbine_rating_MW']= 1.5
        self.sam_defaults['breakpoint_between_base_and_topping_percent']= 0.8
        self.sam_defaults['fuel_usd_per_gal']= 1.5
        self.sam_defaults['rate_of_deliveries']= 10
        self.sam_defaults['turbine_spacing_rotor_diameters']= 4
        self.sam_defaults['depth']= 2.36
        self.sam_defaults['rated_thrust_N']= 589000
        self.sam_defaults['bearing_pressure_n_m2']= 191521
        self.sam_defaults['gust_velocity_m_per_s']= 59.5
        self.sam_defaults['project_size_megawatts']= 150.0
        self.sam_defaults['road_length_adder_m']= 5000
        self.sam_defaults['fraction_new_roads']= 0.33
        self.sam_defaults['road_quality']= 0.6
        self.sam_defaults['line_frequency_hz']= 60
        self.sam_defaults['plant_capacity_MW']= 150.0
        self.sam_defaults['row_spacing_rotor_diameters']= 10
        self.sam_defaults['user_defined_distance_to_grid_connection']= 0
        self.sam_defaults['distance_to_grid_connection_km']= 50
        self.sam_defaults['rsmeans_per_diem']= 99
        self.sam_defaults['fuel_cost_usd_per_gal']= 1.5
        self.sam_defaults['user_defined_home_run_trench']= 0
        self.sam_defaults['trench_len_to_substation_km']= 50
        self.sam_defaults['distance_to_interconnect_mi']= 5
        self.sam_defaults['interconnect_voltage_kV']= 130
        self.sam_defaults['new_switchyard']= True
        self.sam_defaults['critical_speed_non_erection_wind_delays_m_per_s']= 15
        self.sam_defaults['critical_height_non_erection_wind_delays_m']= 10
        self.sam_defaults['road_width_ft']= 20
        self.sam_defaults['road_thickness']= 8
        self.sam_defaults['crane_width']= 12.2
        self.sam_defaults['num_hwy_permits']= 10
        self.sam_defaults['num_access_roads']= 2
        self.sam_defaults['overtime_multiplier']= 1.4
        self.sam_defaults['allow_same_flag']= False
        self.sam_defaults['markup_contingency']= 0.03
        self.sam_defaults['markup_warranty_management']= 0.0002
        self.sam_defaults['markup_sales_and_use_tax']= 0
        self.sam_defaults['markup_overhead']= 0.05
        self.sam_defaults['markup_profit_margin']= 0.05
        self.sam_defaults['season_construct']= ['spring', 'summer', 'fall']
        self.sam_defaults['time_construct']= 'normal'
        self.sam_defaults['hour_day']= {'long': 24, 'normal': 10}
        self.sam_defaults['operational_construction_time']= 10
        self.sam_defaults['operational_hrs_per_day']= 10

        self.project_data = dict()
        self.project_data['crane_specs'] = self.sam_defaults['crane_specs']
        self.project_data['equip'] = self.sam_defaults['equip']
        self.project_data['crew'] = self.sam_defaults['crew']
        self.project_data['equip_price'] = self.sam_defaults['equip_price']
        self.project_data['crew_price'] = self.sam_defaults['crew_price']
        self.project_data['material_price'] = self.sam_defaults['material_price']
        self.project_data['components'] = self.sam_defaults['components']
        self.sam_defaults['project_data'] = self.project_data



    def export_defaults_master_inputs(self):
        return self.sam_defaults


