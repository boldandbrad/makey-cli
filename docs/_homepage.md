# makey-cli

> CLI passkey maker.

A simple and lightweight tool for making secure passkeys in your terminal.

**makey-cli** does not store information, produce logs, or make network
connections. It even avoids printing passkeys in plain-text on screen by
default, instead copying them directly to your clipboard for use.

## Features

- Simple and lightweight
- Relies on the python 3.6+ [`secrets`](https://docs.python.org/3/library/secrets.html)
  module to generate cryptographically strong random passkeys
- Does not produce caches, logs, data stores, or communicate over networks
- Does not display passkeys in plaintext by default
- Makes 16 character long passkeys by default
- Copies new passkeys directly to the clipboard for use
- Can be easily included in scripts to make passkeys in bulk
- Cross platform support - Tested on macOS and Windows (Linux coming soon)
- Free and open source - MIT license

> [Install](install.md "Install") to start making passkeys in your terminal!

<div style="text-align: right"><i>Last updated: {docsify-updated}</i></div>
