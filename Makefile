start:
	pipenv run python .
up: build
	docker-compose up -d
push: build
	docker-compose push git-puller
build: update
	docker-compose build git-puller
update:
	pipenv update
	pipenv lock -r > requirements.txt

