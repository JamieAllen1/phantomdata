from phantomdata.schema_reader import SchemaReader
from phantomdata.yaml_reader import YAMLReader


class SchemaReaderFactory:
    @staticmethod
    def get_reader(format: str) -> SchemaReader:
        if format == "yaml":
            return YAMLReader()
        else:
            raise ValueError(f"Unsupported format: {format}")
