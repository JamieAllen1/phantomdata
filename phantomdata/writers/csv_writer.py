from typing import Optional

import pandas as pd

from phantomdata.logger import get_logger
from phantomdata.writers.data_writer import DataWriter

logger = get_logger(__name__)


class CSVWriter(DataWriter):
    def __init__(self, base_path: Optional[str] = None):
        self.base_path = (
            base_path + "/"
            if base_path and not base_path.endswith("/")
            else ""  # noqa: E501
        )

    def write(self, df: pd.DataFrame, table_name: str) -> None:
        """
        Write a DataFrame to a CSV file.

        :param df: The DataFrame to write.
        :param file_path: The path to the output CSV file.
        """
        file_path = self.base_path + table_name + ".json"
        df.to_csv(file_path, index=False)
        logger.info(f"Data written to {file_path} successfully.")
