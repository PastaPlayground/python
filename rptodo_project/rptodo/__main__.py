# allows us to run package as an exe program using
# python -m rptodo

from rptodo import cli, __app_name__


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
