# glossy
![test](https://github.com/aminekaabachi/glossy/workflows/test/badge.svg?branch=main) [![codecov](https://codecov.io/gh/aminekaabachi/glossy/branch/main/graph/badge.svg)](https://codecov.io/gh/aminekaabachi/glossy) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Glossy enables you to easily build and share data dictionaries. It is an open-source library that allows to define and indicate through code the meaning of terms used to model data through metadata information. It can be integrated with many market data catalog and metadata management solutions.

## Features
* lorem ipsum

## Prerequisites
* [pyenv](https://github.com/pyenv/pyenv)
* [poetry](https://github.com/sdispater/poetry)

## Installation
1. Install [pyenv](https://github.com/pyenv/pyenv).
2. Install the Python versions you want to support using `pyenv`.
  ```sh
  pyenv install 3.6.15
  pyenv install 3.8.12
  pyenv install 3.10.1
  ```
5. Create a virtual env: `pyenv virtualenv 3.8.12 glossy38`
6. Activate virtual env: `pyenv activate glossy38`
7. Install poetry: `pip install poetry`
8. Install dependencies: `poetry install`
9. Edit `pyproject.toml`, update project name, description and author and any other settings you like.

## Usage

Command | Description
--- | ---
`poetry add [package]` | Add package to dependencies.
`poetry add -D [package]` | Add package to dev dependencies.
`poetry run pytest` | Run tests in local Python version.
`poetry run ptw tests glossy --clear` | Watch for file changes and run tests in local Python version.
`poetry run tox` | Run tests in all Python versions defined in `tox.ini`.
`poetry run black .` | Run black code formatter.
`poetry build` | Build sdist and wheel to `/dist`.
`poetry publish` | Publish package to PyPi.

## Continous integration

### GitHub Actions
Tests are run whenever there is a commit, see `.github/workflows/test.yml` for details.

### Code coverage
Enable code coverage reporting to [Codecov](https://codecov.io/) by creating a secret with name `CODECOV_TOKEN` in your repository settings (Settings -> Secrets -> New sectret) and value set to the token created by Codecov.
