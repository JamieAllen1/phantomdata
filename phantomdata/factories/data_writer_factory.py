from phantomdata.writers.csv_writer import CSVWriter
from phantomdata.writers.data_writer import DataWriter
from phantomdata.writers.json_writer import JSONWriter
from phantomdata.writers.parquet_writer import ParquetWriter
from phantomdata.writers.postgres_writer import PostgresWriter


class DataWriterFactory:
    @staticmethod
    def get_writer(format: str, **kwargs) -> DataWriter:
        match format:
            case "csv":
                return CSVWriter(base_path=kwargs["base_path"])
            case "parquet":
                return ParquetWriter(base_path=kwargs["base_path"])
            case "json":
                return JSONWriter(base_path=kwargs["base_path"])
            case "postgres":
                return PostgresWriter(
                    conn_string=kwargs["conn_string"],
                    schema=kwargs.get("schema", "public"),
                )
            case _:
                raise ValueError(f"Unsupported format: {format}")
