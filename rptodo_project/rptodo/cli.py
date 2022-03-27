from typing import Optional

import typer

# import module level var
from rptodo import __app_name__, __version__

# init Typer applicatikon
app = typer.Typer()


def _version_callback(value: bool) -> None:
    # if value returns true
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        # exit app
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        # set command line name for version options
        "--version",
        "-v",
        # provide help message
        help="Show the application's version and exit.",
        # calls function after running version
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
