start:
	pipenv run python .
up:
	docker-compose up -d
push: build
	docker-compose push git-puller
build: update
	docker-compose build git-puller
update:
	pipenv update
	pipenv lock -r > requirements.txt

