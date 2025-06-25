import typer

from phantomdata.processor import processor

app = typer.Typer()


@app.command()
def generate(
    schema: str = typer.Option(..., help="Path to schema (YAML, JSON, etc.)"),  # noqa
    rows: int = typer.Option(1000, help="Number of rows to generate"),  # noqa
    outputpath: str = typer.Option("", help="Output folder name"),  # noqa
    outputformat: str = typer.Option(  # noqa
        "csv", help="Output file format (csv, parquet, json, postgres)"
    ),  # noqa
    dbconnection: str = typer.Option(  # noqa
        "", help="Connection string to target db (if required)"
    ),  # noqa
    dbschema: str = typer.Option("", help="Target DB Schema"),  # noqa
    dbreplace: str = typer.Option(  # noqa
        "replace", help="Replace existing table in the database (if applicable)"  # noqa
    ),  # noqa
    nulls: float = typer.Option(0.0, help="Fraction of nulls to inject"),  # noqa
):
    processor(
        schema=schema,
        rows=rows,
        outputpath=outputpath,
        outputformat=outputformat,
        db_connection=dbconnection,
        db_schema=dbschema,
        db_replace=dbreplace,
        nulls=nulls,
    )


app()
