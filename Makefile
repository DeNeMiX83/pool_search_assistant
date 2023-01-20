include deploy/.env

run:
	make run-api

run-api:
	poetry run uvicorn app.presentation.api.main:app --reload --host $(HOST) --port $(BACKEND_PORT) \
	--log-level ${LOG_LEVEL} 

update-dataset:
	poetry run python -m app.presentation.cli.update_dataset.main

migrate-create:
	poetry run alembic -c deploy/alembic.ini revision --autogenerate

migrate-up:
	poetry run alembic -c deploy/alembic.ini upgrade head

compose-build:
	docker compose -f ./deploy/prod.docker-compose.yml --env-file deploy/.env build

compose-up:
	docker compose -f ./deploy/prod.docker-compose.yml --env-file deploy/.env up

compose-update-dataset:
	docker exec -it ${pool_search_assistant}_backend make update-dataset

docker-rm-volume:
	docker volume rm -f workout_postgres_data