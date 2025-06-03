def test_generate_data():
    from phantomdata.generator import generate_data

    # Test with a simple schema
    schema = {
        "fields": [
            {"name": "id", "type": "integer"},
            {"name": "name", "type": "string"},
            {"name": "email", "type": "string"},
        ]
    }

    df = generate_data(schema, rows=10, null_fraction=0)

    assert len(df) == 10
    assert set(df.columns) == {"id", "name", "email"}
    assert df["id"].dtype == "int64"
    assert df["name"].dtype == "object"
    assert df["email"].dtype == "object"
