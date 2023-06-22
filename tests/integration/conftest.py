import os
import logging
import json

import pytest
from dotenv.main import load_dotenv

from kwil.main import Kwil
from kwil.provider import GRPCProvider


@pytest.fixture(scope="session", autouse=True)
def env():
    load_dotenv()


@pytest.fixture(scope="module")
def wallet():
    private_key = os.getenv("PRIVATE_KEY")
    return Kwil.load_wallet(private_key)


@pytest.fixture(scope="module")
def client(wallet):
    # TODO: spin test services
    logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
    load_dotenv()
    host = os.getenv("NODE_HOST")
    port = os.getenv("NODE_PORT")
    provider = GRPCProvider(f"{host}:{port}")
    return Kwil(provider, wallet)


@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname)


@pytest.fixture(scope="module")
def schema_file():
    return "./test_data/test_schema.json"


@pytest.fixture(scope="module")
def db_name(schema_file):
    with open(f"./tests/integration/{schema_file}", 'r') as json_file:
        schema = json.load(json_file)
        return schema["name"]
