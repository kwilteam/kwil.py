def camel_to_snake(name: str) -> str:
    """Converts a camelCase string to snake_case.

    Args:
        name (str): The camelCase string to convert.

    Returns:
        str: The snake_case string.
    """
    result = ""
    for i, c in enumerate(name):
        if c.isupper():
            if i > 0:
                result += "_"
            result += c.lower()
        else:
            result += c
    return result


def rpc_to_grpc_method_name(rpc_method_name: str) -> str:
    """Converts an RPC method name to a gRPC method name.

    Args:
        rpc_method_name (str): The RPC method name.

    Returns:
        str: The gRPC method name.
    """
    return camel_to_snake(rpc_method_name.split("_")[-1])
