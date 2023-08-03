import logging
from typing import Callable, List

from kwil._utils.rpcs import RPC
from kwil.method import Method
from kwil.module import Module
from kwil.types import (
    DBIdentifier,
    HexAddress,
    TxParam,
    TxReceipt,
    AccountInfo,
    DBSchema,
    ChainConfig,
    CallParam,
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

    ping: Method[Callable[[], bool]] = Method(RPC.kwil_ping)
    get_config: Method[Callable[[], ChainConfig]] = Method(RPC.kwil_getConfig)


class Kwild(BaseKwild):
    """Kwil Chain class"""
    broadcast: Method[Callable[[TxParam], TxReceipt]] = Method(RPC.kwil_broadcast)
    call: Method[Callable[[CallParam], TxReceipt]] = Method(RPC.kwil_call)
    estimate_price: Method[Callable[[TxParam], str]] = Method(RPC.kwil_estimatePrice)
    get_account: Method[Callable[[HexAddress], AccountInfo]] = Method(RPC.kwil_getAccount)
    get_schema: Method[Callable[[DBIdentifier], DBSchema]] = Method(RPC.kwil_getSchema)
    list_databases: Method[Callable[[HexAddress], List[DBSchema]]] = Method(RPC.kwil_listDatabases)
    query: Method[Callable[[DBIdentifier, str], TxReceipt]] = Method(RPC.kwil_query)
