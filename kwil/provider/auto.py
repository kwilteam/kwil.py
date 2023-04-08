from typing import Optional

from kwil.provider import BaseProvider, ProtoBaseProvider


class AutoProvider(BaseProvider):

    default_provider = (
        ProtoBaseProvider
    )

    def __init__(self) -> None:
        self._potential_provider = self.default_provider



