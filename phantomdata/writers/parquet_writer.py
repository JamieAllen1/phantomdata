from typing import Optional

import pandas as pd

from phantomdata.logger import get_logger
from phantomdata.writers.data_writer import DataWriter

logger = get_logger(__name__)


class ParquetWriter(DataWriter):
    def __init__(self, base_path: Optional[str] = None):
        self.base_path = (
            base_path + "/"
            if base_path and not base_path.endswith("/")
            else ""  # noqa: E501
        )

    def write(self, df: pd.DataFrame, table_name: str) -> None:
        """
        Write a DataFrame to a Parquet file.

        :param df: The DataFrame to write.
        :param file_path: The path to the output Parquet file.
        """
        file_path = self.base_path + table_name + ".parquet"
        df.to_parquet(file_path, index=False)
        logger.info(f"Data written to {file_path} successfully.")
