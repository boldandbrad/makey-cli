# makey-cli

[![Build Status](https://api.travis-ci.com/boldandbrad/makey-cli.svg?branch=main)](https://travis-ci.com/github/boldandbrad/makey-cli)
[![codecov](https://codecov.io/gh/boldandbrad/makey-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/boldandbrad/makey-cli)
[![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fboldandbrad.github.io%2Fmakey-cli%2F)](https://boldandbrad.github.io/makey-cli/)
[![PyPI](https://img.shields.io/pypi/v/makey-cli)](https://pypi.org/project/makey-cli/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/makey-cli)

> CLI passkey maker.

A simple and lightweight tool for making secure passkeys in your terminal.

**makey-cli** does not store information, produce logs, or make network
connections. It even avoids printing passkeys in plain-text on screen by
default, instead copying them directly to your clipboard for use.

## Install

```zsh
brew tap boldandbrad/homebrew-tap
brew install makey-cli
```

or

```zsh
pipx install makey-cli
```

or

```zsh
pip install makey-cli
```

> For more details, read the **makey-cli** [install guide](https://boldandbrad.github.io/makey-cli/#/install).

## Usage

```zsh
makey
```

New passkey is copied to your clipboard!

> For more usage details, read the **makey-cli** [usage guide](https://boldandbrad.github.io/makey-cli/#/usage).

## License

Copyright (c) 2021 Bradley Wojcik. Released under the MIT License. See
[LICENSE](LICENSE) for details.
