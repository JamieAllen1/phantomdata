import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from phantomdata.logger import get_logger
from phantomdata.writers.data_writer import DataWriter

logger = get_logger(__name__)


class MSSQLWriter(DataWriter):
    def __init__(self, conn_string: str, schema: str, replace: str):
        """
        Initialize the MSSQLWriter with a SQLAlchemy engine and schema.

        :param conn_string: Connection string to create SQLAlchemy engine
        :param schema: The schema in which to write the data.
        """
        connection_url = URL.create(
            "mssql+pyodbc", query={"odbc_connect": conn_string}
        )  # noqa
        self.engine = create_engine(connection_url)
        self.schema = schema
        self.replace = replace

    def write(self, df: pd.DataFrame, table_name: str) -> None:
        """
        Write a DataFrame to a MSSQL table.

        :param df: The DataFrame to write.
        :param table_name: The table name to write too.
        """

        df.to_sql(
            table_name,
            self.engine,
            schema=self.schema,
            if_exists=self.replace,
            index=False,
        )
        logger.info(
            f"Wrote table '{table_name}' to SQL Server schema '{self.schema}' successfully."  # noqa
        )
