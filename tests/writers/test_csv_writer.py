import pandas as pd
import pytest

from phantomdata.writers.csv_writer import CSVWriter


@pytest.fixture
def dummy_dataframe():
    return pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})


def test_write_calls_to_csv(mocker, dummy_dataframe):
    mock_to_csv = mocker.patch("pandas.DataFrame.to_csv")
    mock_logger = mocker.patch("phantomdata.writers.csv_writer.logger")

    writer = CSVWriter(base_path="fake_path")

    writer.write(dummy_dataframe, "dummy_path")

    mock_to_csv.assert_called_once_with(
        "fake_path/dummy_path.csv", index=False
    )  # noqa: E501
    mock_logger.info.assert_called_once_with(
        "Data written to fake_path/dummy_path.csv successfully."
    )
