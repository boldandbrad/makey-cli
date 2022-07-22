import click
import pyperclip

import string
from secrets import choice

ALWAYS_EXCLUDE = "\"'"
COPIED_STDOUT = "\tNew passkey copied to clipboard!"
DEFAULT_LENGTH = 16


@click.command(help="CLI passkey maker.")
@click.option(
    "-e",
    "--exclude",
    default="",
    is_flag=False,
    help="Characters to exclude. (default \"').",
)
@click.option(
    "-l",
    "--length",
    default=DEFAULT_LENGTH,
    is_flag=False,
    help="Desired passkey length. (default 16).",
)
@click.option(
    "-s",
    "--show",
    default=False,
    is_flag=True,
    help="Print passkey to stdout. Not recommended. (default False).",
)
@click.option(
    "-n",
    "--no-copy",
    default=False,
    is_flag=True,
    help="Do not copy passkey to clipboard. Forces --show. Recommended when piping output in scripts. (default False).",
)
@click.help_option("-h", "--help")
@click.version_option(
    None,  # use version auto discovery via setuptools
    "-v",
    "--version",
    package_name="makey-cli",
    message="%(prog)s-cli, v%(version)s",
)
def cli(exclude: str, length: int, show: bool, no_copy: bool):
    """Main 'makey' command. Makes a passkey and copies it to the clipboard."""

    # determine usable characters
    characters = string.ascii_letters + string.punctuation + string.digits
    exclude += ALWAYS_EXCLUDE
    for char in exclude:
        characters = characters.replace(char, "")

    # make passkey
    passkey = "".join(choice(characters) for _ in range(length))

    # copy passkey to clipboard unless --no-copy given
    if no_copy:
        show = True
    else:
        pyperclip.copy(passkey)

    # print passkey to stdout if --show given, otherwise print success message
    if show:
        print(passkey)
    else:
        print(COPIED_STDOUT)
