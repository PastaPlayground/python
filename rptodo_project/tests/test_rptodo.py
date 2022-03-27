# setting up unit testing
# execute test command in tests/ folder with
# python -m pytest

from typer.testing import CliRunner

from rptodo import __app_name__, __version__, cli

# init CLI runner
runner = CliRunner()

# unit test for app version
def test_version():
    # run test on --version option
    result = runner.invoke(cli.app, ["--version"])
    # result == 0 == ran successfully
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout
