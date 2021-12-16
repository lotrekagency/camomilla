clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

test: clean
	@flake8
	@pytest --cov=camomilla -s --cov-report term-missing

docs: clean
	@sphinx-build -b html ./docs camomilla_docs