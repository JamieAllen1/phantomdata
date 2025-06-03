import pandas as pd
from faker import Faker

fake = Faker()


def generate_data(
    schema_path: str, rows: int, null_fraction: float
) -> pd.DataFrame:  # noqa: E501
    # TEMP: dummy schema logic
    # columns = ["id", "name", "email"]
    data = [
        {
            "id": i,
            "name": fake.name(),
            "email": fake.email() if i % 10 != 0 else None,
        }  # noqa: E501
        for i in range(rows)
    ]
    return pd.DataFrame(data)
