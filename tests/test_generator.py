def test_generate_data():
    from phantomdata.generator import generate_data

    # Test with a simple schema
    schema = [
        {"name": "id", "type": "integer", "domain": "id"},
        {"name": "name", "type": "string", "domain": "name"},
        {"name": "email", "type": "string", "domain": "email"},
        {"name": "age", "type": "integer", "domain": "age"},
        {"name": "is_active", "type": "boolean"},
        {"name": "balance", "type": "decimal", "scale": 5, "precision": 2},
    ]

    df = generate_data(schema, rows=10, null_fraction=0)

    assert len(df) == 10
    assert set(df.columns) == {
        "id",
        "name",
        "email",
        "age",
        "is_active",
        "balance",
    }  # noqa
    assert df["id"].dtype == "int64"
    assert df["name"].dtype == "object"
    assert df["email"].dtype == "object"
    assert df["age"].dtype == "int64"
    assert df["is_active"].dtype == "bool"
    assert df["balance"].dtype == "float64"
