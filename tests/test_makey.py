import pyperclip
from click.testing import CliRunner

from makey.makey import DEFAULT_LENGTH, cli

COPIED_STDOUT = "\tNew passkey copied to clipboard!\n"


def test_makey(mocker):
    mocker.patch("pyperclip.copy")

    runner = CliRunner()
    result = runner.invoke(cli, [])

    assert result.exit_code == 0
    pyperclip.copy.assert_called_once()
    assert result.stdout == COPIED_STDOUT


def test_makey_default_length(mocker):
    mocker.patch("pyperclip.copy")

    runner = CliRunner()
    result = runner.invoke(cli, ["--show"])

    assert result.exit_code == 0
    pyperclip.copy.assert_called_once()

    passkey = result.stdout.rstrip()

    assert len(passkey) == DEFAULT_LENGTH
    assert "'" not in passkey
    assert '"' not in passkey


def test_makey_exclude(mocker):
    mocker.patch("pyperclip.copy")

    runner = CliRunner()
    result = runner.invoke(cli, ["-s", "-e", "&"])

    assert result.exit_code == 0
    pyperclip.copy.assert_called_once()

    passkey = result.stdout.rstrip()

    assert len(passkey) == DEFAULT_LENGTH
    assert "'" not in passkey
    assert '"' not in passkey
    assert "&" not in passkey


def test_makey_length(mocker):
    mocker.patch("pyperclip.copy")

    runner = CliRunner()
    result = runner.invoke(cli, ["--show", "-l", 20])

    assert result.exit_code == 0
    pyperclip.copy.assert_called_once()

    passkey = result.stdout.rstrip()

    assert len(passkey) == 20
    assert "'" not in passkey
    assert '"' not in passkey


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0


def test_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
