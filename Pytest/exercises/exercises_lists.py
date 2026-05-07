def get_first(fellowship: list[str]) -> str:
    """Returns the first member of the fellowship. Example: get_first(['Frodo', 'Sam']) -> 'Frodo'"""
    return fellowship[0]


def get_last(fellowship: list[str]) -> str:
    """Returns the last member of the fellowship. Example: get_last(['Frodo', 'Sam']) -> 'Sam'"""
    return fellowship[-1]


def count_members(fellowship: list[str]) -> int:
    """Returns the number of members in the fellowship. Example: count_members(['Frodo', 'Sam']) -> 2"""
    return len(fellowship)


def add_member(fellowship: list[str], name: str) -> list[str]:
    """Adds a new member to the end of the fellowship and returns it. Example: add_member(['Frodo'], 'Sam') -> ['Frodo', 'Sam']"""
    fellowship.append(name)
    return fellowship


def remove_member(fellowship: list[str], name: str) -> list[str]:
    """Removes a member from the fellowship by name and returns it. Example: remove_member(['Frodo', 'Sam'], 'Sam') -> ['Frodo']"""
    fellowship.remove(name)
    return fellowship


def sort_fellowship(fellowship: list[str]) -> list[str]:
    """Returns a new alphabetically sorted list without modifying the original. Example: sort_fellowship(['Sam', 'Frodo']) -> ['Frodo', 'Sam']"""
    return sorted(fellowship)


def is_member(fellowship: list[str], name: str) -> bool:
    """Returns True if the name is in the fellowship. Example: is_member(['Frodo', 'Sam'], 'Frodo') -> True"""
    return name in fellowship


def reverse_fellowship(fellowship: list[str]) -> list[str]:
    """Returns a new list in reverse order without modifying the original. Example: reverse_fellowship(['Frodo', 'Sam']) -> ['Sam', 'Frodo']"""
    return fellowship[::-1]


def merge_fellowships(fellowship1: list[str], fellowship2: list[str]) -> list[str]:
    """Merges two fellowships into one. Example: merge_fellowships(['Frodo'], ['Sam']) -> ['Frodo', 'Sam']"""
    return fellowship1 + fellowship2


def remove_duplicates(fellowship: list[str]) -> list[str]:
    """Removes duplicates from the fellowship preserving order. Example: remove_duplicates(['Frodo', 'Sam', 'Frodo']) -> ['Frodo', 'Sam']"""
    return list(dict.fromkeys(fellowship))
