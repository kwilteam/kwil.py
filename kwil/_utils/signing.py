from eth_account import Account
from eth_account.signers.local import LocalAccount


def load_wallet(private_key_str: str) -> LocalAccount:
    return Account.from_key(private_key_str)
