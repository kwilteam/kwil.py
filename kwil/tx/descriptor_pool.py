from .v1 import (
    account_pb2,
    broadcast_pb2,
    config_pb2,
    dataset_pb2,
    list_pb2,
    ping_pb2,
    price_pb2,
    query_pb2,
    tx_pb2
)
#
# from google.protobuf.descriptor_pool import DescriptorPool
#
#
# kwild_descriptor_pool = DescriptorPool()
# kwild_descriptor_pool.Add(account_pb2.DESCRIPTOR)
# kwild_descriptor_pool.Add(broadcast_pb2.BroadcastResponse)
# kwild_descriptor_pool.Add(config_pb2.GetConfigResponse)
# kwild_descriptor_pool.Add(dataset_pb2.Dataset)
# kwild_descriptor_pool.Add(list_pb2.ListDatabasesResponse)
# kwild_descriptor_pool.Add(ping_pb2.PingResponse)
# kwild_descriptor_pool.Add(price_pb2.EstimatePriceResponse)
# kwild_descriptor_pool.Add(query_pb2.QueryResponse)
# kwild_descriptor_pool.Add(tx_pb2.Tx)