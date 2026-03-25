import pandas as pd
from faker import Faker

from phantomdata.logger import get_logger

logger = get_logger(__name__)

fake = Faker()


def generate_data(
    schema: list, rows: int, null_fraction: float
) -> pd.DataFrame:  # noqa: E501

    # Build a dataframe to store the data
    df = pd.DataFrame()

    for col in schema:
        col_name = col.get("name")
        col_type = col.get("type")
        col_domain = col.get("domain", None)
        col_length = col.get("length", None)
        col_scale = col.get("scale", 5)
        col_precision = col.get("precision", 2)
        col_min = col.get("min", None)
        col_max = col.get("max", None)
        col_values = col.get("values", None)

        # Generate data based on type
        if col_domain == "id":
            data = [i + 1 for i in range(rows)]
        elif col_domain == "fixed":
            data = [col.get("value", "fixed_value") for i in range(rows)]
        elif col_domain == "list":
            data = [
                fake.word(ext_word_list=col_values) for i in range(rows)  # noqa: E501
            ]  # noqa: E501
        elif col_domain == "name":
            data = [fake.name() for i in range(rows)]
        elif col_domain == "email":
            data = [fake.email() for i in range(rows)]
        elif col_domain == "age":
            data = [fake.random_int(min=18, max=80) for i in range(rows)]
        elif col_domain == "date":
            data = [
                fake.date_this_year(before_today=True, after_today=True)
                for i in range(rows)
            ]
        elif col_domain == "datetime":
            data = [
                fake.date_time_this_year(before_now=True, after_now=True)
                for i in range(rows)
            ]
        elif col_domain == "time":
            data = [fake.time() for i in range(rows)]
        elif col_type == "integer":
            data = [
                (
                    fake.random_int(min=col_min, max=col_max)
                    if col_min is not None
                    else fake.random_int()
                )
                for _ in range(rows)
            ]
        elif col_type == "decimal":
            data = [
                fake.random_number(digits=col_scale) / (10**col_precision)
                for _ in range(rows)
            ]  # noqa: E501
        elif col_type == "string":
            if col_domain == "upper":
                data = [
                    (
                        fake.text(max_nb_chars=5).upper()[:col_length]
                        if col_length < 5
                        else fake.text(max_nb_chars=col_length).upper()
                    )
                    for _ in range(rows)
                ]
            else:
                data = [
                    (
                        fake.text(max_nb_chars=5)[:col_length]
                        if col_length < 5
                        else fake.text(max_nb_chars=col_length)
                    )
                    for _ in range(rows)
                ]
        elif col_type == "boolean":
            data = [fake.boolean() for _ in range(rows)]

        logger.debug(
            f"Generating {col_name} with type {col_type} and domain {col_domain}"  # noqa: E501
        )

        df = df.assign(z=data)  # Assign the generated data to the DataFrame
        df.rename(columns={"z": col_name}, inplace=True)  # Rename the column

    # print(f"DataFrame size is {df.size}")
    # print(df.info())

    return df
