import typer

from phantomdata.generator import generate_data
from phantomdata.schema_loader import load_schema
from phantomdata.writer import writer

app = typer.Typer()


@app.command()
def generate(
    schema: str = typer.Option(..., help="Path to schema (YAML, JSON, etc.)"),  # noqa
    rows: int = typer.Option(1000, help="Number of rows to generate"),  # noqa
    output: str = typer.Option("output.csv", help="Output file name"),  # noqa
    fileformat: str = typer.Option(  # noqa
        "csv", help="Output file format (csv, parquet, json)"
    ),  # noqa
    nulls: float = typer.Option(0.0, help="Fraction of nulls to inject"),  # noqa
):
    """Generate synthetic data from a schema."""
    columns = load_schema(schema)

    df = generate_data(columns, rows, nulls)
    # df.to_csv(output, index=False)
    writer(df, output, fileformat)
    typer.echo(f"✅ Wrote {rows} rows to {output}")


app()
