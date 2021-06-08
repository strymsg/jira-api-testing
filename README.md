# Jira API basic testing

### Requirements

- python3
- make
- python3 virtualenv

## Setup

Install virtualenv and project's dependencies

```
virtualenv --python=python3 venv

# activate
source venv/bin/activate

pip install -r requirements.txt
```

Rename `common/configs.sample.json` to `common/configs.json` and make changes to that file if neccesary.

Running commands:

- tests: `make test`
- lint: `make lint`

Optionally can also run tests with `pytests`

```
pytest

# optionally verbose
pytest -s
```
