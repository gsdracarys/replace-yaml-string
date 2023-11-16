.PHONY: setup run clean test

venv:
	@echo "Creating virtual environment..."
	python3 -m venv venv

setup: venv
	@echo "Installing dependencies..."
	@. venv/bin/activate; pip install -r requirements.txt
	@echo "Copying files into venv..."
	@cp -R * venv/

run: setup
	@echo "Running script..."
	@. venv/bin/activate; python src/vaultmock.py

clean:
	@echo "Cleaning up..."
	@rm -rf venv
	@find . -name "*.pyc" -type f -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} +

test: setup
	@echo "Running tests..."
	@. venv/bin/activate; python -m unittest tests/test_vaultmock.py
