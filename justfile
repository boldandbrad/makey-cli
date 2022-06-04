
# activate venv
venv:
    . .venv/bin/activate

# install makey-cli
install:
    pip install .

# install editable
dev:
    pip install -e .

# build dist
build:
    python setup.py sdist bdist_wheel

# generate homebrew formula
brew: install
    poet -f makey-cli >> formula.rb

# run all tests
test: install
    pytest

# run all tests with coverage
test-cov: install
    pytest --cov-report=xml --cov=./makey/

# remove artifacts
cleanup:
    rm -f .coverage
    rm -f coverage.xml
    rm -f formula.rb
    rm -rf .pytest_cache
    rm -rf build
    rm -rf dist
    rm -rf *.egg-info
    rm -rf makey/__pycache__
    rm -rf tests/__pycache__