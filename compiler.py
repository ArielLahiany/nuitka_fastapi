# Python modules.
import os


def main() -> None:
    """
    Main entrypoint for Nuitka compilation.
    :return: None.
    """

    cmd = (
        "python -m nuitka --onefile -o server manage.py"
    )
    os.system(cmd)


if __name__ == "__main__":
    main()
