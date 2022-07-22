# Changelog

All notable changes to **makey-cli** will be documented here.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/ "Keep a Changelog"),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html "Semantic Versioning").

## Unreleased

### Added

- New `-n`/`--no-copy` option to send passkeys to stdout instead of the clipboard.

### Deprecated

- The `-s`/`--show` is slated to be removed in a future major release.

## [1.2.0] - 2022-05-03

### Added

- New `-e`/`--exclude` option to make passkeys without certain characters.
- Ability to install makey-cli with Homebrew! See [Install Guide](install.md
  "Install Guide").

## Changed

- Quote characters (`"` and `'`) are now ALWAYS excluded from passkeys

## [1.1.0] - 2021-11-24

### Changed

- Updated dependency Click from v7.x to v8.x
- Code formatting and structure

### Fixed

- `makey --version` Correctly works again with latest dependencies.

### Removed

- Support for python versions 3.6 and 3.7

## [1.0.0] - 2020-10-29

### Added

- `makey` Create a secure and randomized passkey, copied directly to your clipboard.
  - `-l`/`--length <int>` Specify a custom passkey length.
  - `-s`/`--show` Send passkey to stdout in addition to the clipboard.
- `makey --version` Check current installed version.
- `makey --help` Print out cli usage.
