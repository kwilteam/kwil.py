import logging
from typing import Callable, List

from kwil._utils.rpcs import GRPC
from kwil.method import Method
from kwil.module import Module
from kwil.types import (
    DBIdentifier,
    HexAddress,
    TxParams,
    TxReceipt,
    AccountInfo,
    DBSchema,
    ServiceConfig,
)


class BaseKwild(Module):
    """Kwil Chain base class"""

    logger = logging.getLogger("kwil.BaseKwild")

    def __init__(self, kwil):
        self.kwil = kwil
        self.cfg = self.get_config()
        self.logger.debug("KwilChain config: %s", self.cfg)

    # def get_block(self, block_id):
    #     return self.kwil.manager.request_blocking(GRPC.kwil_getBlock, [block_id])

    ping: Method[Callable[[], bool]] = Method(GRPC.kwil_ping)
    get_config: Method[Callable[[], ServiceConfig]] = Method(GRPC.kwil_getConfig)


class Kwild(BaseKwild):
    """Kwil Chain class"""

    get_schema: Method[Callable[[DBIdentifier], DBSchema]] = Method(GRPC.kwil_getSchema)
    list_database: Method[Callable[[HexAddress], List[DBSchema]]] = Method(
        GRPC.kwil_listDatabase
    )
    get_account: Method[Callable[[HexAddress], AccountInfo]] = Method(
        GRPC.kwil_getAccount
    )
    broadcast: Method[Callable[[TxParams], TxReceipt]] = Method(GRPC.kwil_broadcast)
    estimate_price: Method[Callable[[TxParams], str]] = Method(GRPC.kwil_estimatePrice)
    query: Method[Callable[[DBIdentifier, str], TxReceipt]] = Method(GRPC.kwil_query)
