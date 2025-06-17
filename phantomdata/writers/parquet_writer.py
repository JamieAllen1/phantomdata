import pandas as pd

from phantomdata.writers.data_writer import DataWriter
from phantomdata.logger import get_logger

logger = get_logger(__name__)


class ParquetWriter(DataWriter):

    def write(self, df: pd.DataFrame, file_path: str) -> None:
        """
        Write a DataFrame to a Parquet file.

        :param df: The DataFrame to write.
        :param file_path: The path to the output Parquet file.
        """
        df.to_parquet(file_path, index=False)
        logger.info(f"Data written to {file_path} successfully.")
