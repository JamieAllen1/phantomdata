from phantomdata.factories.data_writer_factory import DataWriterFactory
from phantomdata.factories.schema_reader_factory import SchemaReaderFactory
from phantomdata.generator import generate_data


def processor(
    schema: str,
    rows: int = 1000,
    output: str = "output.csv",
    fileformat: str = "csv",
    nulls: float = 0.0,
):
    """Generate synthetic data from a schema."""
    reader = SchemaReaderFactory.get_reader("yaml")
    columns = reader.read(schema)
    # columns = load_schema(schema)

    df = generate_data(columns, rows, nulls)
    writer = DataWriterFactory.get_writer(fileformat)
    writer.write(df, output)
