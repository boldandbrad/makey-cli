
# activate venv
venv:
    . .venv/bin/activate

# install meeple-cli from local
install:
    pip install -q ."[test]"

# install meeple-cli via flit
flit-install:
    pip install flit
    flit install

# install editable
dev-install:
    pip install -q -e .

# lint and format
lint:
    pre-commit run --show-diff-on-failure --all-files

# run all tests
test: install
    pytest

# run all tests with coverage
test-cov: install
    pytest -v --cov-report xml --cov makey

# build dist
build:
    flit build

# serve docs on localhost
serve-docs:
    docsify serve docs

# generate homebrew formula
brew: install
    poet -f makey-cli >> formula.rb

# remove artifacts
cleanup:
    rm -f .coverage
    rm -f coverage.xml
    rm -f formula.rb
    rm -rf .pytest_cache
    rm -rf build
    rm -rf dist
    rm -rf *.egg-info
    rm -rf src/makey/__pycache__
    rm -rf tests/__pycache__
    rm -rf .ruff_cache
