import pandas as pd
import pytest

from phantomdata.writers.postgres_writer import PostgresWriter


@pytest.fixture
def dummy_dataframe():
    return pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})


def test_write_calls_to_sql(mocker, dummy_dataframe):
    mock_to_sql = mocker.patch("pandas.DataFrame.to_sql")
    mock_logger = mocker.patch("phantomdata.writers.postgres_writer.logger")

    writer = PostgresWriter(
        conn_string="postgresql://user:pass@localhost/db",
        schema="public",
        replace="replace",
    )
    writer.write(
        dummy_dataframe,
        "dummy_table",
    )

    mock_to_sql.assert_called_once_with(
        "dummy_table",
        writer.engine,
        schema="public",
        if_exists="replace",
        index=False,  # noqa: E501
    )
    mock_logger.info.assert_called_once_with(
        "Wrote table 'dummy_table' to Postgres schema 'public' successfully."
    )
