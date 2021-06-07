# Jira API basic testing

## Setup

Install virtualenv and project's dependencies

```
virtualenv --python=python3 venv

# activate
source venv/bin/activate

pip install -r requirements.txt
```

Rename `common/configs.sample.json` to `common/configs.json` and make changes to that file if neccesary.

Run tests:

```
pytest

# optionally verbose
pytest -s
```
