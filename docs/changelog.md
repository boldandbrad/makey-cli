# Changelog

All notable changes to **makey-cli** will be documented here.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/ "Keep a Changelog"),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html "Semantic Versioning").

## [Unreleased]

## [1.3.0] - 2023-04-19

### Added

- `CI` - GitHub Actions CI.
  - `python-test` - Lint and Test package, and publish test coverage to Codecov.
  - `python-publish` - Publish package to PYPI.
  - `docs-publish` - Publish docs to GitHub Pages.
- `CI` - `pre-commit` lint hooks.

### Changed

- `GENERAL` - Code formatting and folder structure.
- `BUILD` - Upgrade from `setup.py` to `pyproject.toml` with `flit` build tool.

### Removed

- `CI` - Travis CI.

## [1.2.0] - 2022-05-03

### Added

- `makey`: `-e`/`--exclude` - Exclude given characters from passkeys.
- `INSTALL` - Install makey-cli with Homebrew! See [Install Guide](install.md "Install Guide").

## Changed

- `makey` - Quote characters (`"` and `'`) are now ALWAYS excluded from passkeys.

## [1.1.0] - 2021-11-24

### Changed

- `DEPENDENCY` - Update Click from v7.x to v8.x.
- `GENERAL` - Code formatting and structure.

### Fixed

- `makey`: `--version` - Correctly works again with latest dependencies.

### Removed

- `GENERAL` - Support for python versions 3.6 and 3.7.

## [1.0.0] - 2020-10-29

### Added

- `makey` - Create a secure and randomized passkey, copied directly to your clipboard.
  - `-l/--length` - Specify a custom passkey length.
  - `-s/--show` - Send passkey to stdout in addition to the clipboard.
  - `--version` - Check current installed version.
  - `--help` - Print out cli usage.
