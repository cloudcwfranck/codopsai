from unittest import mock

from click.testing import CliRunner

from codops.cli import app


def test_run_empty_command() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["run"])
    assert result.exit_code != 0
    assert "Nothing to run" in result.output


@mock.patch("codops.cli.run_prompt", return_value="pong")
def test_run_command(mock_run) -> None:  # type: ignore[no-redef]
    runner = CliRunner()
    result = runner.invoke(app, ["run", "ping"])
    assert result.exit_code == 0
    assert result.output.strip() == "pong"


def test_summary_default() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["summary"])
    assert result.exit_code == 0
    assert "codops CLI" in result.output


def test_summary_project() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["summary", "--project"])
    assert result.exit_code == 0
    assert "Project summary" in result.output
