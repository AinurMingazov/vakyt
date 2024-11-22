
fmt:
	poetry run ruff format .
	poetry run ruff check . --fix --unsafe-fixes
	poetry run isort pyproject.toml

lint:
	poetry run ruff check .
	poetry run mypy .
	poetry run isort pyproject.toml --check

