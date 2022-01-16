# How to contribute 

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
5. Create a virtual env: `pyenv virtualenv 3.8.12 lexy38`
6. Activate virtual env: `pyenv activate lexy38`
7. Install poetry: `pip install poetry`
8. Install dependencies: `poetry install`
9. Edit `pyproject.toml`, update project name, description and author and any other settings you like.

## Usage

Command | Description
--- | ---
`poetry add [package]` | Add package to dependencies.
`poetry add -D [package]` | Add package to dev dependencies.
`poetry run pytest` | Run tests in local Python version.
`poetry run ptw tests lexy --clear` | Watch for file changes and run tests in local Python version.
`poetry run tox` | Run tests in all Python versions defined in `tox.ini`.
`poetry run black .` | Run black code formatter.
`poetry build` | Build sdist and wheel to `/dist`.
`poetry publish` | Publish package to PyPi.

###  Pull request

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from `develop` if it exists, else from `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them!
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's [interactive rebase](https://help.github.com/articles/interactive-rebase). Create a new branch if necessary.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's `develop` branch if there is one, else go for `master`!
- ...
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete your extra branch(es).

And last but not least: Always write your commit messages in the present tense. Your commit message should describe what the commit, when applied, does to the code – not what you did to the code.