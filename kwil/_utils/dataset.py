import hashlib


def generate_dbi(owner: str, name: str) -> str:
    """Generate a database identifier."""
    bs = bytearray()
    bs.extend(name.lower().encode())
    bs.extend(owner.lower().encode())
    return "x{0}".format(hashlib.sha224(bs).hexdigest())
