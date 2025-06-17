import typer

from phantomdata.processor import processor

app = typer.Typer()


@app.command()
def generate(
    schema: str = typer.Option(..., help="Path to schema (YAML, JSON, etc.)"),  # noqa
    rows: int = typer.Option(1000, help="Number of rows to generate"),  # noqa
    outputpath: str = typer.Option("", help="Output folder name"),  # noqa
    fileformat: str = typer.Option(  # noqa
        "csv", help="Output file format (csv, parquet, json)"
    ),  # noqa
    nulls: float = typer.Option(0.0, help="Fraction of nulls to inject"),  # noqa
):
    processor(
        schema=schema,
        rows=rows,
        outputpath=outputpath,
        fileformat=fileformat,
        nulls=nulls,
    )


app()
