import pytest

from kwil._utils.action import encode_action_args


def test_encode_action_args():
    result = encode_action_args([{"$name": "aha"}])
    assert result == [{"$name": "ZmFoYQ=="}]

    result = encode_action_args([{"$age": 18}])
    assert result == [{"$age": "ZxIAAAAAAAAA"}]
