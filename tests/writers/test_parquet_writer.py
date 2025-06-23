import pandas as pd
import pytest

from phantomdata.writers.parquet_writer import ParquetWriter


@pytest.fixture
def dummy_dataframe():
    return pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})


def test_write_calls_to_parquet(mocker, dummy_dataframe):
    mock_to_parquet = mocker.patch("pandas.DataFrame.to_parquet")
    mock_logger = mocker.patch("phantomdata.writers.parquet_writer.logger")

    writer = ParquetWriter(base_path="fake_path")

    writer.write(dummy_dataframe, "dummy_path")

    mock_to_parquet.assert_called_once_with(
        "fake_path/dummy_path.parquet", index=False
    )  # noqa: E501
    mock_logger.info.assert_called_once_with(
        "Data written to fake_path/dummy_path.parquet successfully."
    )
