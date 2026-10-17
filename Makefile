.PHONY: install test lint clean

install:
	pip install -r requirements.txt

test:
	pytest -v

clean:
	rm -rf dist/ build/ *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
