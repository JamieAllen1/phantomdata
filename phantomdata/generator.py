import pandas as pd
from faker import Faker

fake = Faker()


def generate_data(
    schema: list, rows: int, null_fraction: float
) -> pd.DataFrame:  # noqa: E501

    # Build a dataframe to store the data
    df = pd.DataFrame()

    for col in schema:
        col_name = col["name"]
        col_type = col["type"]

        # Generate data based on type
        if col_name == "id":
            data = [i + 1 for i in range(rows)]
        elif col_name == "name":
            data = [fake.name() for i in range(rows)]
        elif col_name == "email":
            data = [fake.email() for i in range(rows)]
        elif col_name == "age":
            data = [fake.random_int(min=18, max=80) for i in range(rows)]
        elif col_type == "integer":
            data = [fake.random_int() for _ in range(rows)]
        elif col_type == "string":
            data = [fake.text(max_nb_chars=100) for _ in range(rows)]
        # elif col_type == "float":
        #     data.append(
        #       [fake.random_number(digits=5, fix_len=True)
        #       for _ in range(rows)]
        #       )

        df = df.assign(z=data)  # Assign the generated data to the DataFrame
        df.rename(columns={"z": col_name}, inplace=True)  # Rename the column

    # print(f"DataFrame size is {df.size}")
    # print(df.info())

    return df
