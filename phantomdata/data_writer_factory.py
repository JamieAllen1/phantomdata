from phantomdata.csv_writer import CSVWriter
from phantomdata.data_writer import DataWriter
from phantomdata.json_writer import JSONWriter
from phantomdata.parquet_writer import ParquetWriter


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
