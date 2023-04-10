import hashlib

from kwil.types import DBIdentifier


def generate_dbi(owner: str, name: str) -> DBIdentifier:
    """Generate a database identifier."""
    bs = bytearray()
    bs.extend(name.lower().encode())
    bs.extend(owner.lower().encode())
    formatted = "x{0}".format(hashlib.sha224(bs).hexdigest())
    return DBIdentifier(formatted)
