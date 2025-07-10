import typer
from pubmed_fetcher.main import run

app = typer.Typer()

@app.command()
def main(
    query: str = typer.Argument(..., help="Search query for PubMed"),
    file: str = typer.Option("", "--file", "-f", help="Output CSV filename"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode")
):
    print("CLI started ✅")
    run(query=query, filename=file, debug=debug)

if __name__ == "__main__":
    app()
