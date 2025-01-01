
fmt:
	poetry run ruff format .
	poetry run ruff check . --fix --unsafe-fixes
	poetry run isort pyproject.toml

lint:
	poetry run ruff check .
	poetry run mypy .
	poetry run isort pyproject.toml --check

rebuild:
	sudo docker-compose down -v
	sudo docker-compose build --no-cache
	sudo docker-compose up
