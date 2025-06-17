import pandas as pd

from phantomdata.logger import get_logger
from phantomdata.writers.data_writer import DataWriter

logger = get_logger(__name__)


class CSVWriter(DataWriter):

    def write(self, df: pd.DataFrame, file_path: str) -> None:
        """
        Write a DataFrame to a CSV file.

        :param df: The DataFrame to write.
        :param file_path: The path to the output CSV file.
        """
        df.to_csv(file_path, index=False)
        logger.info(f"Data written to {file_path} successfully.")
