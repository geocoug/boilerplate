VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
TEST = pytest

$(VENV)/bin/activate: requirements.txt
	python3 -m venv .venv
	$(PIP) install -r requirements.txt

run: $(VENV)/bin/activate
	$(PYTHON) app/main.py

clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf app/__pycache__
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf logs

update: $(VENV)/bin/activate
	$(PIP) install -U pip
	$(PYTHON) -m pre_commit autoupdate

test: $(VENV)/bin/activate
	$(PYTHON) -m $(TEST) -v

lint: $(VENV)/bin/activate
	$(PYTHON) -m pre_commit install --install-hooks
	$(PYTHON) -m pre_commit run --all-files
