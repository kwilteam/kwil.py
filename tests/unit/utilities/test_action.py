from kwil._utils.action import encode_action_inputs


def test_encode_action_inputs():
    result = encode_action_inputs([{"$name": "aha"}])
    assert result == [{"$name": "ZmFoYQ=="}]

    result = encode_action_inputs([{"$age": 18}])
    assert result == [{"$age": "ZxIAAAAAAAAA"}]
