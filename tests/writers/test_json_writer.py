import pandas as pd
import pytest

from phantomdata.writers.json_writer import JSONWriter


@pytest.fixture
def dummy_dataframe():
    return pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})


def test_write_calls_to_json(mocker, dummy_dataframe):
    mock_to_json = mocker.patch("pandas.DataFrame.to_json")
    mock_logger = mocker.patch("phantomdata.writers.json_writer.logger")

    writer = JSONWriter(base_path="fake_path")

    writer.write(dummy_dataframe, "dummy_path")

    mock_to_json.assert_called_once_with(
        "fake_path/dummy_path.json", orient="records", lines=True
    )  # noqa: E501
    mock_logger.info.assert_called_once_with(
        "Data written to fake_path/dummy_path.json successfully."
    )
