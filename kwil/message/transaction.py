"""
Support serializing kwil transaction body to message to be signed
"""

template_v0 = """%s

PayloadType: %s
PayloadDigest: %x
Fee: %s
Nonce: %d
Salt: %x

Kwil 🖋
"""

def serialize(txParam)