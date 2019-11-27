import sqlite3

from .SqliteLoggerException import SqliteLoggerException

"""
This module is for a very simple logging system with an SQLite database
"""

# These are not docstrings. They are placed in triple quotes to make them
# more readable. Their format follows the structure of the Excel sheets
# they store.

create_table_statements = [
    """
    CREATE TABLE IF NOT EXISTS costs_by_module_type_operation(    
        project_id_with_serial TEXT,
        num_turbines INTEGER,
        turbine_rating_mw REAL,
        module TEXT,
        operation_id TEXT,
        type_of_cost TEXT,
        cost_per_turbine REAL,
        cost_per_project REAL,
        usd_per_kw_per_project REAL
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS details(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id_with_serial TEXT,
        module TEXT,
        name TEXT,
        unit TEXT,
        numeric_value REAL,
        non_numeric_value TEXT
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS error_log(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id_with_serial TEXT,
        message TEXT
    );
    """
]


class SqliteLogger:
    """
    This class is for storing error messages and result tables in a small
    sqlite database.
    """

    def __init__(self, db_filename):
        """
        The constructor takes the filename of the database to which
        the table should be written.

        The constructor creates the database named by the filename and creates
        the tables for that database.

        In order to not lock the database unnecessarily, each method gets its
        own connection. Hence, the connection is not stored as an instance
        attribute.

        This class is assumed to be called with a non-existent filename so that
        it can create a fresh database. It won't destroy data that already exists,
        but the schema assumes that all rows in all the tables specify the same
        model run.

        Parameters
        ----------
        db_filename : str
            The name of the database file to write to.
        """
        self.db_filename = db_filename

    def create_tables(self):
        """
        This opens the database and creates tables so that records can be
        inserted later. It won't delete data that already exists in the
        database.

        Raises
        ------
        SqliteLoggerException
            A SqliteLoggerException is raised when there is an error
            creating the database.
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_filename)
            with conn:
                for create_table_statement in create_table_statements:
                    conn.execute(create_table_statement)
        except sqlite3.Error as e:
            raise SqliteLoggerException(f'SqliteLogger: Could not create database and tables at {self.db_filename}')
        finally:
            if conn is not None:
                conn.close()

    def insert_costs_by_module_type_operation(self, rows):
        """
        This method must be called after the create_tables() method is called.
        It requires the tables created in create_tables() to be present for
        data to be inserted into them.

        Parameters
        ----------
        rows : list [dict]
            This is a list of dictionaries, with each dictionary being a row
            to write into the actual database table.

        Raises
        ------
        SqliteLoggerException
            This exception is raised if there are sqlite errors when the insert
            is attempted.
        """
        insert_statement = """INSERT INTO costs_by_module_type_operation VALUES(
            :project_id_with_serial, :num_turbines, 
            :turbine_rating_MW, :module, :operation_id, 
            :type_of_cost, :cost_per_turbine, 
            :cost_per_project, :usd_per_kw_per_project
            )"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_filename)
            with conn:
                cursor = conn.cursor()
                for row in rows:
                    cursor.execute(insert_statement, row)
        except sqlite3.Error as e:
            raise SqliteLoggerException(f'SqliteLogger: Could not insert into table costs_by_module_type_operation in {self.db_filename}')
        finally:
            if conn is not None:
                conn.close()
