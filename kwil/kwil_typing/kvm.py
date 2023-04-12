from typing import NewType

DBIdentifier = NewType("DBIdentifier", str)

HexStr = NewType("HexStr", str)
HexAddress = NewType("HexAddress", HexStr)
