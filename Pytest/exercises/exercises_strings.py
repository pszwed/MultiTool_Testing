def greet(name: str) -> str:
    """Returns a greeting message. Example: greet('Frodo') -> 'Hello, Frodo!'"""
    return f"Hello, {name}!"


def to_uppercase(name: str) -> str:
    """Returns the name in uppercase. Example: to_uppercase('Frodo') -> 'FRODO'"""
    return name.upper()


def is_hobbit(name: str) -> bool:
    """Returns True if the name ends with 'o'. Example: is_hobbit('Frodo') -> True"""
    return name.endswith("o")


def get_initials(first_name: str, last_name: str) -> str:
    """Returns initials in format 'F.B.'. Example: get_initials('Frodo', 'Baggins') -> 'F.B.'"""
    if not first_name or not last_name:
        raise ValueError("Name cannot be empty!")
    return f"{first_name[0]}.{last_name[0]}."


def count_letter_o(name: str) -> int:
    """Counts occurrences of letter 'o' (case-insensitive). Example: count_letter_o('Frodo') -> 2"""
    return name.lower().count("o")


def replace_name(sentence: str, old: str, new: str) -> str:
    """Replaces a name in a sentence. Example: replace_name('Frodo goes', 'Frodo', 'Sam') -> 'Sam goes'"""
    return sentence.replace(old, new)


def split_sentence(sentence: str) -> list:
    """Splits a sentence into a list of words. Example: split_sentence('Frodo Baggins') -> ['Frodo', 'Baggins']"""
    return sentence.split()


def join_fellowship(names: list) -> str:
    """Joins a list of names with ', '. Example: join_fellowship(['Frodo', 'Sam']) -> 'Frodo, Sam'"""
    return ", ".join(names)


def is_letters_only(name: str) -> bool:
    """Returns True if the name contains only letters. Example: is_letters_only('Frodo') -> True"""
    return name.isalpha()


def is_capitalized(name: str) -> bool:
    """Returns True if the name starts with a capital letter. Example: is_capitalized('Frodo') -> True"""
    if not name:
        return False
    return name[0].isupper()


def count_chars_no_spaces(sentence: str) -> int:
    """Returns the number of characters excluding spaces. Example: count_chars_no_spaces('Frodo Baggins') -> 12"""
    without_space = sentence.replace(" ", "")
    return len(without_space)


def reverse_name(name: str) -> str:
    """Returns the name reversed. Example: reverse_name('Frodo') -> 'odarF'"""
    return name[::-1]
