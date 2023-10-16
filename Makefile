.PHONY: docs clean init test

init:
	python -m venv venv
	source venv/bin/activate && pip install -e .

docs:
	echo "Please implement me!"

test:
	python -m unittest discover -s tests -t .
