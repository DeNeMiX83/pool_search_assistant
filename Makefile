include deploy/.env

run:
	make run-api

run-api:
	poetry run gunicorn app.presentation.api.main:app --reload -b $(HOST):$(BACKEND_PORT) \
	--worker-class uvicorn.workers.UvicornWorker \
	--log-level $(LOG_LEVEL)


update-dataset:
	poetry run python -m app.presentation.cli.update_dataset.main

migrate-create:
	poetry run alembic -c deploy/alembic.ini revision --autogenerate

migrate-up:
	poetry run alembic -c deploy/alembic.ini upgrade head

compose-build:
	docker compose -f ./deploy/prod.docker-compose.yml --env-file deploy/.env build

compose-up:
	docker compose -f ./deploy/prod.docker-compose.yml --env-file deploy/.env -p $(PROJECT_NAME) up

.PHONY: compose-logs
compose-logs:
	docker compose -f $./deploy/prod.docker-compose.yml --env-file deploy/.env \
	-p $(PROJECT_NAME) logs -f

compose-update-dataset:
	docker exec -it $(PROJECT_NAME)_backend make update-dataset

docker-rm-volume:
	docker volume rm -f $(PROJECT_NAME)_database_data