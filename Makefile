run-linter:
	pre-commit run

setup:
	pipenv shell \
	pipenv install

run-db:
	docker-compose up -d --build

run-app:
	uvicorn app.main:app --reload

sql-run:
	PGPASSWORD=rybasher2281899 psql -U rybasher -d diplom_db -h localhost
