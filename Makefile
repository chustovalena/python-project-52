install:
	uv sync

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

migrate:
	uv run manage.py migrate

collectstatic:
	uv run manage.py collectstatic

dev:
	uv run manage.py runserver

lint:
	ruff check

sonar:
	pytest --cov=. --cov-report=xml
	pysonar --sonar-token=$(SONAR_TOKEN)
