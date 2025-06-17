from phantomdata.factories.data_writer_factory import DataWriterFactory
from phantomdata.factories.schema_reader_factory import SchemaReaderFactory
from phantomdata.generator import generate_data
from phantomdata.logger import get_logger

logger = get_logger(__name__)


def processor(
    schema: str,
    rows: int = 1000,
    outputpath: str = "examples",
    fileformat: str = "csv",
    nulls: float = 0.0,
):
    """Generate synthetic data from a schema."""
    reader = SchemaReaderFactory.get_reader("yaml")
    writer = DataWriterFactory.get_writer(fileformat)

    tables = reader.read(schema)
    logger.debug(f"Schema read: {tables}")

    for table in tables:
        logger.debug(f"Processing table: {table}")
        tablename = table.get("name", "default_table")
        row_count = table.get("count", None)
        columns = table.get("columns", [])
        if row_count is None:
            row_count = rows

        df = generate_data(columns, row_count, nulls)
        # writer.write(df, "../../" + outputpath + "/" + tablename + "." + fileformat) # noqa: E501
        writer.write(df, tablename + "." + fileformat)
