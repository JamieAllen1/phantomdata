import yaml

from phantomdata.logger import get_logger
from phantomdata.readers.schema_reader import SchemaReader

logger = get_logger(__name__)


class YAMLReader(SchemaReader):
    """
    A class to read YAML files and return the schema as a list of dictionaries.
    """

    def read(self, path) -> list:
        """
        Reads the YAML file and returns the schema.
        """
        schema = None
        generator_queue = []
        with open(path, "r") as file:
            # Load the schema using yaml.safe_load for YAML files
            if path.endswith(".yaml") or path.endswith(".yml"):
                schema = yaml.safe_load(file)
            else:
                raise ValueError(
                    "Unsupported schema format. Only YAML is supported."
                )  # noqa: E501
        if schema is not None:
            # Ensure the schema is a dictionary and extract the columns
            logger.debug(schema)
            tables = schema["tables"]
            for table in tables:
                table_item = table.get("table", {})
                table_name = table_item.get("name", "default_table")
                table_count = table_item.get("count")
                table_columns = table_item.get("columns", [])
                logger.debug(
                    f"Processing table: {table_name} with count: {table_count} and columns: {table_columns}"  # noqa: E501
                )
                item = {
                    "name": table_name,
                    "count": table_count,
                    "columns": table_columns,
                }
                generator_queue.append(item)
            logger.debug(f"Generator queue: {generator_queue}")

        else:
            raise ValueError("Failed to load schema from the provided path.")

        return generator_queue
