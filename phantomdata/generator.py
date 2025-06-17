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

        # Generate data based on type
        if col_domain == "id":
            data = [i + 1 for i in range(rows)]
        elif col_domain == "name":
            data = [fake.name() for i in range(rows)]
        elif col_domain == "email":
            data = [fake.email() for i in range(rows)]
        elif col_domain == "age":
            data = [fake.random_int(min=18, max=80) for i in range(rows)]
        elif col_type == "integer":
            data = [fake.random_int() for _ in range(rows)]
        elif col_type == "decimal":
            data = [
                fake.random_number(digits=col_scale) / (10**col_precision)
                for _ in range(rows)
            ]  # noqa: E501
        elif col_type == "string":
            data = [fake.text(max_nb_chars=col_length) for _ in range(rows)]
        elif col_type == "boolean":
            data = [fake.boolean() for _ in range(rows)]

        logger.debug(f"Generating {col_name} with type {col_type} and domain {col_domain}")

        df = df.assign(z=data)  # Assign the generated data to the DataFrame
        df.rename(columns={"z": col_name}, inplace=True)  # Rename the column

    # print(f"DataFrame size is {df.size}")
    # print(df.info())

    return df
