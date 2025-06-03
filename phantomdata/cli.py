import typer

from phantomdata.generator import generate_data
from phantomdata.schema_loader import load_schema

app = typer.Typer()


@app.command()
def generate(
    schema: str = typer.Option(..., help="Path to schema (YAML, JSON, etc.)"),  # noqa
    rows: int = typer.Option(1000, help="Number of rows to generate"),  # noqa
    output: str = typer.Option("output.csv", help="Output file name"),  # noqa
    nulls: float = typer.Option(0.0, help="Fraction of nulls to inject"),  # noqa
):
    """Generate synthetic data from a schema."""
    df = generate_data(schema, rows, nulls)
    df.to_csv(output, index=False)
    typer.echo(f"✅ Wrote {rows} rows to {output}")


@app.command()
def getschema():
    schema = load_schema()
    typer.echo(f"Extracted schema: {schema}")


app()
