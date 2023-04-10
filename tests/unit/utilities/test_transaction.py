from kwil._utils.transaction import generate_tx_hash
from kwil.types import TxPayloadType, Nonce


def test_generate_tx_hash():
    tx_hash = generate_tx_hash(
        b"payload",
        TxPayloadType.DEPLOY_DATABASE,
        "0",
        Nonce(1),
    )
    assert tx_hash.hex() == \
           "4e8855a27265fbcc98b98cd9519799893ad937312bfbda70a5852474dd6c96aea0bb973936c3d601a2cc5b935709bd6d"


