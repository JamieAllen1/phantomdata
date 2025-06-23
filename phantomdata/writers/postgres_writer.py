import pandas as pd
from sqlalchemy import create_engine

from phantomdata.logger import get_logger
from phantomdata.writers.data_writer import DataWriter

logger = get_logger(__name__)


class PostgresWriter(DataWriter):
    def __init__(self, conn_string: str, schema: str = "public"):
        """
        Initialize the PostgresWriter with a SQLAlchemy engine and schema.

        :param conn_string: Connection string to create SQLAlchemy engine
        :param schema: The schema in which to write the data.
        """
        self.engine = create_engine(conn_string)
        self.schema = schema

    def write(self, df: pd.DataFrame, table_name: str) -> None:
        """
        Write a DataFrame to a JSON file.

        :param df: The DataFrame to write.
        :param file_path: The path to the output JSON file.
        """

        df.to_sql(
            table_name,
            self.engine,
            if_exists="replace",
            index=False,
            schema=self.schema,
        )
        logger.info(
            f"Wrote table '{table_name}' to Postgres schema '{self.schema}' successfully."  # noqa: E501
        )
