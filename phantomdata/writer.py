import pandas as pd


def writer(df: pd.DataFrame, file_path: str, file_format: str = "csv") -> None:
    """
    Write a DataFrame to a file in the specified format.

    :param df: The DataFrame to write.
    :param file_path: The path to the output file.
    :param file_format: The format of the output file ('csv', 'parquet', 'json'). # noqa
    """
    if file_format == "csv":
        write_to_csv(df, file_path)
    elif file_format == "parquet":
        write_to_parquet(df, file_path)
    elif file_format == "json":
        write_to_json(df, file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")


def write_to_csv(df: pd.DataFrame, file_path: str) -> None:
    """
    Write a DataFrame to a CSV file.

    :param df: The DataFrame to write.
    :param file_path: The path to the output CSV file.
    """
    df.to_csv(file_path, index=False)
    print(f"Data written to {file_path} successfully.")


def write_to_parquet(df: pd.DataFrame, file_path: str) -> None:
    """
    Write a DataFrame to a Parquet file.

    :param df: The DataFrame to write.
    :param file_path: The path to the output Parquet file.
    """
    df.to_parquet(file_path, index=False)
    print(f"Data written to {file_path} successfully.")


def write_to_json(df: pd.DataFrame, file_path: str) -> None:
    """
    Write a DataFrame to a JSON file.

    :param df: The DataFrame to write.
    :param file_path: The path to the output JSON file.
    """
    df.to_json(file_path, orient="records", lines=True)
    print(f"Data written to {file_path} successfully.")
