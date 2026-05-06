def show_type(value):
    """
    Returns a string describing the type and processed value.
    Supports: int, float, str, list.
    Returns None for unsupported types.
    """
    if isinstance(value, bool):
        return f"Bool: {value}"
    elif isinstance(value, (int, float)):
        return f"Number: {value * 2}"
    elif isinstance(value, str):
        return f"String: {value.upper()}"
    elif isinstance(value, list):
        return f"List has {len(value)} elements"
    else:
        return None