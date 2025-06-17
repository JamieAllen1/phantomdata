import pandas as pd

from phantomdata.data_writer import DataWriter


class ParquetWriter(DataWriter):

    def write(self, df: pd.DataFrame, file_path: str) -> None:
        """
        Write a DataFrame to a Parquet file.

        :param df: The DataFrame to write.
        :param file_path: The path to the output Parquet file.
        """
        df.to_parquet(file_path, index=False)
        print(f"Data written to {file_path} successfully.")
