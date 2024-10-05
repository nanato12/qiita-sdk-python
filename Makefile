.PHONY: init
init:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

.PHONY: lint
lint:
	ruff --version
	ruff check
	ruff format --check
	mypy .

.PHONY: fmt
fmt:
	ruff --version
	ruff format
	ruff check --fix

.PHONY: generate
generate:
	rm -rf docs
	rm -rf qiita/v2
	rm -rf test
	npx @openapitools/openapi-generator-cli generate \
		-i qiita-openapi/openapi.yml \
		-g python \
		-o . \
		-c config.yml \
		--git-repo-id qiita-api-sdk-python \
		--git-user-id nanato12
