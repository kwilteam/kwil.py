.DEFAULT_GOAL := help
.PHONY: git-sync protosrc proto help clean-build clean-pyc

help:
	# 20s is the width of the first column
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

protofiles := $(wildcard protos/kwil/*/v0/*.proto)
## generate python source file list from proto files
protosrc: $(protofiles)

git-sync: ## sync git submodules
	git submodule update --remote

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

clean: clean-build clean-pyc

release: clean ## build package and upload a release
	python -m build
	ls -l dist
	python -m twine upload --repository pypi dist/*

test: ## run tests quickly with the default Python
	pytest tests

test-all: ## run tests on every Python version
	tox

lint: ## check style with flake8
	tox -e lint

dist: clean ## package
	python -m build
	ls -l dist
