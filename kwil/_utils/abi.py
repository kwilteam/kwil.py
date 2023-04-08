from typing import Sequence, Any

from toolz import curry
import itertools


from eth_typing import TypeStr


@curry
def map_abi_data(
        types: Sequence[TypeStr],
        data: Sequence[Any],
) -> Any:
    pipeline = itertools.chain(

