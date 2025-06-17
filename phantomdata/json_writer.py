import pandas as pd

from phantomdata.data_writer import DataWriter


class JSONWriter(DataWriter):

    def write(self, df: pd.DataFrame, file_path: str) -> None:
        """
        Write a DataFrame to a JSON file.

        :param df: The DataFrame to write.
        :param file_path: The path to the output JSON file.
        """
        df.to_json(file_path, orient="records", lines=True)
        print(f"Data written to {file_path} successfully.")
