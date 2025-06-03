from pyiceberg.catalog import load_catalog


def cast_field(field_type):
    print(f"Type{type(field_type)}")
    return type(field_type)
    # match type(field_type):
    #     case (field_type, pyiceberg.types.LongType):
    #         return "bigint"
    #     case isinstance(field_type, pyiceberg.types.IntegerType):
    #         return "bigint"
    #     case isinstance(field_type, pyiceberg.types.LongType):
    #         return "bigint"
    #     case isinstance(field_type, pyiceberg.types.BooleanType):
    #         return "boolean"
    #     case isinstance(field_type, pyiceberg.types.FloatType):
    #         return "float"
    #     case isinstance(field_type, pyiceberg.types.DoubleType):
    #         return "double"
    #     case isinstance(field_type, pyiceberg.types.DateType):
    #         return "date"
    #     case isinstance(field_type, pyiceberg.types.TimestampType):
    #         return "timestamp"
    #     case _:
    #         raise ValueError(f"Unsupported field type: {field_type}")


def load_schema():
    generator_schema = []

    warehouse_path = "/Users/jamieallen/tmp/warehouse"
    catalog = load_catalog(
        "default",
        **{
            "type": "sql",
            "uri": f"sqlite:///{warehouse_path}/pyiceberg_catalog.db",
            "warehouse": f"file://{warehouse_path}",
        },
    )
    table = catalog.load_table("default.taxi_dataset")

    schema = table.schema().as_struct()
    for field in schema.fields:
        print(field.name, field.field_type)
        schema_item = {  # noqa
            "name": field.name,
            "type": cast_field(field.field_type),
            # "nullable": field.is_optional(),
        }  # noqa
        # generator_schema.append(schema_item)

    return generator_schema
