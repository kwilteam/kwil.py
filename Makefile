.DEFAULT_GOAL := help
.PHONY: protosrc proto help clean-build clean-pyc

help:
	# 20s is the width of the first column
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

protofiles := $(wildcard protos/kwil/*/v0/*.proto)
protosrc: $(protofiles) ## generate python source from proto files

proto: protosrc ## generate python source from proto files and compile
	python -m grpc_tools.protoc -I ./proto --python_out=. --pyi_out=. --grpc_python_out=. ./proto/kwil/tx/v1/*.proto

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test: ## run tests quickly with the default Python
	pytest tests

test-all: ## run tests on every Python version
	tox

lint: ## check style with flake8
	tox -e lint

