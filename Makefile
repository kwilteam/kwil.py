.DEFAULT_GOAL := proto

protofiles := $(wildcard protos/kwil/*/v0/*.proto)

protosrc: $(protofiles)

proto: protosrc
	python -m grpc_tools.protoc -I ./proto --python_out=. --pyi_out=. --grpc_python_out=. ./proto/kwil/tx/v1/*.proto

.PHONY: protosrc proto