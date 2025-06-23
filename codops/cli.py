"""CLI for codops."""

from __future__ import annotations

import click

from .openai_client import run_prompt


@click.group()
def app() -> None:
    """Codops command line interface."""


@app.command()
@click.argument("nl_command", nargs=-1)
def run(nl_command: tuple[str, ...]) -> None:
    """Interpret NL_COMMAND via OpenAI and print the result."""
    prompt = " ".join(nl_command)
    if not prompt:
        click.echo("Nothing to run")
        raise SystemExit(1)
    try:
        result = run_prompt(prompt)
    except Exception as exc:  # pragma: no cover - network errors
        click.echo(f"Error: {exc}")
        raise SystemExit(1)
    click.echo(result)


@app.command()
@click.option("--project", is_flag=True, help="Generate project summary")
def summary(project: bool) -> None:
    """Show summary information."""
    if project:
        click.echo("Project summary coming soon.")
    else:
        click.echo("codops CLI")


if __name__ == "__main__":  # pragma: no cover
    app()
