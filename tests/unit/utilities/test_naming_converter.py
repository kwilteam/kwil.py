import pytest

from kwil._utils.naming_converter import camel_to_snake


@pytest.mark.parametrize(
    "name,expected",
    [
        ("camelCase", "camel_case"),
        ("FirstName", "first_name"),
        ("alllowercase", "alllowercase"),
        ("camelCaseWithNumber1", "camel_case_with_number1"),
    ]
)
def test_camel_to_snake(name, expected):
    assert camel_to_snake(name) == expected
