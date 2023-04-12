import hashlib
from eth_account.signers.local import LocalAccount

from kwil.types import TxParams, TxPayloadType, Nonce
from kwil._utils.signature import sign


# generate_tx_hash generates a hash of the transaction
# it does this by hashing the payload type, payload, fee, and nonce
def generate_tx_hash(
    payload: bytes, payload_type: TxPayloadType, fee: str, nonce: Nonce
) -> bytes:
    data = bytearray()

    # convert payload type to bytes
    payload_type_bytes = payload_type.to_bytes(4, byteorder="little")
    data.extend(payload_type_bytes)

    # hash payload
    payload_hash = hashlib.sha384(payload).digest()
    data.extend(payload_hash)

    # add fee
    data.extend(fee.encode())

    # convert nonce to bytes
    nonce_bytes = nonce.to_bytes(8, byteorder="little")
    data.extend(nonce_bytes)

    return hashlib.sha384(data).digest()


def sign_tx(params: TxParams, wallet: LocalAccount) -> TxParams:
    tx_hash = generate_tx_hash(
        params["payload"],
        params["payloadType"],
        params["fee"],
        params["nonce"],
    )

    params["hash"] = tx_hash
    params["signature"] = sign(tx_hash, wallet.key)
    params["sender"] = wallet.address
    return params
