import argparse


def create_argument_parser(description: str) -> argparse.ArgumentParser:
    """
    Create an argument parser that can be extended.

    Parameters:
    description (str): The description for the argument parser

    Returns:
    ArgumentParser: an argument parser.
    """

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-p",
        "--page",
        type=str,
        default="",
        help='page name in the format "platform/alias_command.md"',
    )
    parser.add_argument(
        "-S",
        "--sync",
        action="store_true",
        default=False,
        help="synchronize each translation's alias page (if exists) with that of English page",
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        default="",
        help='language in the format "ll" or "ll_CC" (e.g. "fr" or "pt_BR")',
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        default=False,
        help="show what changes would be made without actually modifying the pages",
    )

    return parser
