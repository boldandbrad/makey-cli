import os

from click.testing import CliRunner
import pyperclip

from makey.makey import cli


DEFAULT_LENGTH = 16


def test_makey():
    if "TRAVIS" not in os.environ:
        runner = CliRunner()
        result = runner.invoke(cli, [])
        assert result.exit_code == 0
        assert result.stdout == "\tNew passkey copied to clipboard.\n"
        assert len(pyperclip.paste()) == DEFAULT_LENGTH


def test_makey_with_length():
    if "TRAVIS" not in os.environ:
        runner = CliRunner()
        result = runner.invoke(cli, ["-l", "20"])
        assert result.exit_code == 0
        assert result.stdout == "\tNew passkey copied to clipboard.\n"
        assert len(pyperclip.paste()) == 20


def test_makey_with_show():
    if "TRAVIS" not in os.environ:
        runner = CliRunner()
        result = runner.invoke(cli, ["-s"])
        assert result.exit_code == 0
        assert len(result.stdout.replace("\n", "")) == DEFAULT_LENGTH
        assert len(pyperclip.paste()) == DEFAULT_LENGTH


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0


def test_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
