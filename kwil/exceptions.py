class BadResponseFormat(ValueError, KeyError):
    # Inherits from KeyError and ValueError for backwards compatibility
    """
    Raised when the response format is incorrect.
    """
    pass


class InvalidAddress(ValueError):
    """
    The supplied address is invalid.
    """

    pass


class CannotHandleRequest(ValueError):
    """
    The provider cannot handle the request.
    """

    pass
