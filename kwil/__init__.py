import sys
import pkg_resources

from kwil.main import Kwil
from kwil.provider import GRPCProvider

if sys.version_info < (3, 9):
    raise EnvironmentError("Python 3.9 or above is required. ")

__version__ = pkg_resources.get_distribution("kwil").version

__all__ = [
    "__version__",
    "Kwil",
    "GRPCProvider",
]
