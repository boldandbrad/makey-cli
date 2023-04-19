# Usage Guide

Discover all available **makey-cli** options with `makey --help`.

## Make a passkey

Makey makes making a passkey super simple and quick. Make and copy a secure 16
character passkey to your clipboard with just the root command!

```zsh
makey
```

### Options

- `-e`, `--exclude` - Characters to exclude from passkey. (`v1.2.0+`)

  > Be default, passkeys contain a random mix of [ascii letter](https://docs.python.org/3/library/string.html#string.ascii_letters),
  > [digit](https://docs.python.org/3/library/string.html#string.digits),
  > and [punctuation](https://docs.python.org/3/library/string.html#string.punctuation)
  > characters. However, quote characters (`"`/`'`) are ALWAYS excluded.

  ```zsh
  makey -e %$
  ```

- `-l`, `--length` - Make a passkey of specified length. Default: 16.

  ```zsh
  makey -l 12
  ```

- `-s`, `--show` - Print the made passkey to stdout. Default: false.

  ```zsh
  makey -s
  ```

- `-v`, `--version` - Print the installed makey-cli version.

<div style="text-align: right"><i>Last updated: {docsify-updated}</i></div>
