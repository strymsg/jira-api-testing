# Based on: https://gist.github.com/lumengxi/0ae4645124cd4066f676
.PHONY: help prepare-dev test lint run doc

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make prepare-dev"
	@echo "       prepare development environment, udse only once"
	@echo "make test"
	@echo "       run tests"
	@echo "make lint"
	@echo "       run pylint and mypy"
	@echo "make run"
	@echo "       run project"
	@echo "make doc"
	@echo "       build sphinx documentation"

prepare-dev:
	python3 -m pip install virtualenv
	make venv

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -e .
	touch $(VENV_NAME)/bin/activate


test: venv
	${PYTHON} -m pytest

# Notice the "-" character tells make to ignore errors from command given
lint: venv
	@echo
	@echo "flake8-----------"
	@echo
	-${PYTHON} -m flake8 api/ common/ utils/ tests/
	@echo
	@echo "pylint-----------"
	@echo
	-${PYTHON} -m pylint api common utils tests
	@echo
	@echo "pycodestyle-----------"
	@echo
	-pycodestyle api
run: venv
	${PYTHON} app.py

doc: venv
	$(VENV_ACTIVATE) && cd docs; make html