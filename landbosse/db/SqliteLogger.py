import sqlite3

"""
This module is for a very simple logging system with an SQLite database
"""

# These are not docstrings. They are placed in triple quotes to make them
# more readable. Their format follows the structure of the Excel sheets
# they store.

create_table_statements = [
    """
    CREATE TABLE IF NOT EXISTS costs_by_module_type_operation(    
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id_with_serial TEXT,
        number_of_turbines INTEGER,
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


class SqliteLoggerException(Exception):
    """
    This exception is raised for errors that occur when processing
    SQLite files.

    It has no custom implementation. It is here to provide a class that
    can be specifically caught in an except statement.

    See also: https://docs.python.org/3/library/exceptions.html
    """
    pass


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

    def _create_tables(self):
        """
        The starting underscore in the method name means that it should
        not be called except by __init__().

        This opens the database and creates tables.
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_filename)
            with conn:
                for create_table_statement in create_table_statements:
                    conn.execute(create_table_statement)
        except sqlite3.Error as e:
            raise SqliteLoggerException('SqliteLogger could not create the database file and tables.')
        finally:
            if conn is not None:
                conn.close()
