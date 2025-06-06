import yaml


def load_schema(path: str) -> list:
    """
    Takes a schema path and returns a list of dictionaries
    representing the schema.
    """
    schema = None
    with open(path, "r") as file:
        # Load the schema using yaml.safe_load for YAML files
        if path.endswith(".yaml") or path.endswith(".yml"):
            schema = yaml.safe_load(file)
        else:
            raise ValueError(
                "Unsupported schema format. Only YAML is supported."
            )  # noqa: E501
    if schema is not None:
        # Ensure the schema is a dictionaries
        if isinstance(schema, dict):
            generator_schema = schema["table"]["columns"]
        else:
            raise ValueError("Schema must be a dictionary.")
    else:
        raise ValueError("Failed to load schema from the provided path.")

    return generator_schema
