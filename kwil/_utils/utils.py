from typing import Any, Callable, List

from toolz import curry


@curry
def apply_validator_at_index(
    fn: Callable[..., Any], index: int, value: List[Any]
) -> Any:
    if index >= len(value):
        raise IndexError(
            "Not enough values to apply validator. {0}<{1}".format(len(value), index)
        )
    for i, item in enumerate(value):
        if i == index:
            fn(item)

    return value
