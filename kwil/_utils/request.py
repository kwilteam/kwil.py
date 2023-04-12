import os
from collections import OrderedDict
import threading
import logging
from typing import Any, Dict, List

from kwil._utils.naming_converter import camel_to_snake, rpc_to_grpc_method_name
from kwil._utils.grpc import Client as GRPCClient
from kwil.types import URI

DEFAULT_CACHE_SIZE = 20
DEFAULT_TIMEOUT = 10
logger = logging.getLogger(__name__)


class ConnectionCache:
    def __init__(self, size: int):
        self.size = size
        self._connections: OrderedDict[str, Any] = OrderedDict()

    def cache(self, key: str, value: Any) -> Dict[str, Any]:
        evicted_items = None

        if key not in self._connections:
            while len(self._connections) >= self.size:
                if evicted_items is None:
                    evicted_items = {}
                # FIFO
                k, v = self._connections.popitem(last=False)
                evicted_items[k] = v
        self._connections[key] = value
        return evicted_items

    def get_cache_entry(self, key: str) -> Any:
        return self._connections[key]

    def clear(self) -> None:
        self._connections.clear()

    def __contains__(self, item: str) -> bool:
        return item in self._connections

    def __len__(self) -> int:
        return len(self._connections)


_conn_cache = ConnectionCache(size=DEFAULT_CACHE_SIZE)
_conn_cache_lock = threading.Lock()


def _get_conn(endpoint_uri: str) -> Any:
    cache_key = f"grpc:{threading.get_ident()}:{endpoint_uri}"

    if cache_key in _conn_cache:
        return _conn_cache.get_cache_entry(cache_key)

    # cache new connection
    evicted_items = None
    with _conn_cache_lock:
        if cache_key not in _conn_cache:
            evicted_items = _conn_cache.cache(cache_key, GRPCClient(endpoint_uri))
            logger.debug("connection cached: %s", endpoint_uri)

    if evicted_items is not None:
        evicted_conns = evicted_items.values()
        for conn in evicted_conns:
            logger.debug("Cache full. Evicted conn: %s", conn)

        # close evicted connections after timeout in separate thread
        threading.Timer(
            DEFAULT_TIMEOUT + 0.1, _close_evicted_conns, args=[evicted_conns]
        )

    return _conn_cache.get_cache_entry(cache_key)


def _close_evicted_conns(conns: List[GRPCClient]) -> None:
    for conn in conns:
        conn.close()
        logger.debug("Evicted conn closed: %s", conn)


def grpc_request(endpoint_uri, method, args):
    conn = _get_conn(endpoint_uri)
    method = rpc_to_grpc_method_name(method)
    method = camel_to_snake(method)
    grpc_method = getattr(conn, method)
    # catch exceptions here
    resp = grpc_method(*args)
    return resp


def get_default_grpc_endpoint() -> URI:
    return URI(os.environ.get("KWIL_GRPC_PROVIDER_URI", "localhost:50051"))
