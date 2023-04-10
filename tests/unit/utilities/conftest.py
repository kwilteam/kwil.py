import pytest


@pytest.fixture(scope="module")
def private_key() -> str:
    return "f1aa5a7966c3863ccde3047f6a1e266cdc0c76b399e256b8fede92b1c69e4f4e"
