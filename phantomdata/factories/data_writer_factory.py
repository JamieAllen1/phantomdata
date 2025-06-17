from phantomdata.writers.csv_writer import CSVWriter
from phantomdata.writers.data_writer import DataWriter
from phantomdata.writers.json_writer import JSONWriter
from phantomdata.writers.parquet_writer import ParquetWriter


class DataWriterFactory:
    @staticmethod
    def get_writer(format: str) -> DataWriter:
        if format == "csv":
            return CSVWriter()
        elif format == "parquet":
            return ParquetWriter()
        elif format == "json":
            return JSONWriter()
        else:
            raise ValueError(f"Unsupported format: {format}")
