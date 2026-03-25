from phantomdata.factories.data_writer_factory import DataWriterFactory
from phantomdata.factories.schema_reader_factory import SchemaReaderFactory
from phantomdata.generator import generate_data
from phantomdata.logger import get_logger

logger = get_logger(__name__)


def processor(
    schema: str,
    rows: int = 1000,
    outputpath: str = "examples",
    outputformat: str = "csv",
    db_connection: str = "",
    db_schema: str = "",
    db_replace: str = "",
    nulls: float = 0.0,
):
    """Generate synthetic data from a schema."""
    reader = SchemaReaderFactory.get_reader("yaml")
    if outputformat == "postgres":
        writer = DataWriterFactory.get_writer(
            outputformat,
            conn_string=db_connection,
            schema=db_schema,
            replace=db_replace,
        )
    elif outputformat == "mssql":
        writer = DataWriterFactory.get_writer(
            outputformat,
            conn_string=db_connection,
            schema=db_schema,
            replace=db_replace,
        )
    else:
        writer = DataWriterFactory.get_writer(
            outputformat, base_path=outputpath + "/"
        )  # noqa: E501

    tables = reader.read(schema)
    logger.debug(f"Schema read: {tables}")

    for table in tables:
        logger.debug(f"Processing table: {table}")
        table_name = table.get("name", "default_table")
        row_count = table.get("count", None)
        columns = table.get("columns", [])
        if row_count is None:
            row_count = rows

        df = generate_data(columns, row_count, nulls)

        writer.write(df, table_name)
