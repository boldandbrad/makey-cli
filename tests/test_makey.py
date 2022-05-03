import os

from click.testing import CliRunner
import pyperclip

from makey.makey import cli


DEFAULT_LENGTH = 16
COPIED_STDOUT = "\tNew passkey copied to clipboard!\n"


def test_makey():
    if "TRAVIS" not in os.environ:
        runner = CliRunner()
        result = runner.invoke(cli, [])
        assert result.exit_code == 0

        passkey = pyperclip.paste()

        assert result.stdout == COPIED_STDOUT
        assert len(passkey) == DEFAULT_LENGTH
        assert '"' not in passkey
        assert "'" not in passkey


def test_makey_with_exclude():
    if "TRAVIS" not in os.environ:
        runner = CliRunner()
        result = runner.invoke(cli, ["-e", "&"])
        assert result.exit_code == 0

        passkey = pyperclip.paste()

        assert result.stdout == COPIED_STDOUT
        assert len(passkey) == DEFAULT_LENGTH
        assert "&" not in passkey


def test_makey_with_length():
    if "TRAVIS" not in os.environ:
        runner = CliRunner()
        result = runner.invoke(cli, ["-l", "20"])
        assert result.exit_code == 0

        passkey = pyperclip.paste()

        assert result.stdout == COPIED_STDOUT
        assert len(passkey) == 20


def test_makey_with_show():
    if "TRAVIS" not in os.environ:
        runner = CliRunner()
        result = runner.invoke(cli, ["-s"])
        assert result.exit_code == 0

        passkey = pyperclip.paste()
        printedkey = result.stdout.replace("\n", "")

        assert len(passkey) == DEFAULT_LENGTH
        assert passkey == printedkey


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0


def test_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
