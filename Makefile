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
	uv run ruff check

sonar:
	uv run pytest --cov=. --cov-report=xml
	uv run pysonar --sonar-token=$(SONAR_TOKEN)

makemessages:
	uv run manage.py makemessages -l ru

compilemessages:
	uv run manage.py compilemessages --ignore=.venv

docker:
	docker compose up --build -d
