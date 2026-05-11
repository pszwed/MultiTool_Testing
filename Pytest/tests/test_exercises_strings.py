import pytest
from exercises.exercises_strings import (
    greet,
    to_uppercase,
    is_hobbit,
    get_initials,
    count_letter_o,
    replace_name,
    split_sentence,
    join_fellowship,
    is_letters_only,
    is_capitalized,
    count_chars_no_spaces,
    reverse_name,
)


class TestGreet:
    @pytest.mark.parametrize(
        "name, expected",
        [
            ("Frodo", "Hello, Frodo!"),
            ("Sam", "Hello, Sam!"),
            ("Gandalf", "Hello, Gandalf!"),
        ],
    )
    def test_greet(self, name, expected):
        result = greet(name)
        assert result == expected

    def test_greet_returns_string(self):
        result = greet("Frodo")
        assert isinstance(result, str)


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Frodo", "FRODO"),
        ("Legolas", "LEGOLAS"),
        ("sauron", "SAURON"),
        ("", ""),
    ],
)
def test_to_uppercase(name, expected):
    result = to_uppercase(name)
    assert result == expected


class TestIsHobbit:
    def test_frodo_is_hobbit(self):
        result = is_hobbit("Frodo")
        assert result is True

    def test_bilbo_is_hobbit(self):
        result = is_hobbit("Bilbo")
        assert result is True

    def test_gandalf_is_not_hobbit(self):
        result = is_hobbit("Gandalf")
        assert result is False

    def test_empty_string(self):
        result = is_hobbit("")
        assert result is False


class TestGetInitials:
    @pytest.mark.parametrize(
        "first_name, last_name, expected",
        [
            ("Frodo", "Baggins", "F.B."),
            ("Gandalf", "Szary", "G.S."),
            ("Samwise", "Gamgee", "S.G."),
        ],
    )
    def test_get_initials(self, first_name, last_name, expected):
        result = get_initials(first_name, last_name)
        assert result == expected

    def test_get_initials_empty(self):
        with pytest.raises(ValueError):
            get_initials("", "Baggins")


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Frodo", 2),
        ("Gandalf", 0),
        ("FRODO", 2),
        ("Bilbo", 1),
    ],
)
def test_count_letter_o(name, expected):
    result = count_letter_o(name)
    assert result == expected


def test_replace_name():
    sentence = "Frodo goes to Mordor"
    old = "Frodo"
    new = "Sam"
    result = replace_name(sentence, old, new)
    assert result == "Sam goes to Mordor"


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("Frodo Baggins hobbit", ["Frodo", "Baggins", "hobbit"]),
        ("Frodo", ["Frodo"]),
        ("Frodo  Sam", ["Frodo", "Sam"]),
    ],
)
def test_split_sentence(sentence, expected):
    result = split_sentence(sentence)
    assert result == expected


@pytest.mark.parametrize(
    "names, expected",
    [
        (["Frodo", "Sam", "Gandalf"], "Frodo, Sam, Gandalf"),
        (["Frodo"], "Frodo"),
        ([], ""),
    ],
)
def test_join_fellowship(names, expected):
    result = join_fellowship(names)
    assert result == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Frodo", True),
        ("Frodo2", False),
        ("Frodo Baggins", False),
        ("", False),
    ],
)
def test_is_letters_only(name, expected):
    result = is_letters_only(name)
    assert result == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Frodo", True),
        ("frodo", False),
        ("FRODO", True),
        ("", False),
    ],
)
def test_is_capitalized(name, expected):
    result = is_capitalized(name)
    assert result == expected


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("Frodo Baggins", 12),
        ("Frodo", 5),
        ("", 0),
        ("Frodo Baggins hobbit", 18),
    ],
)
def test_count_chars_no_spaces(sentence, expected):
    result = count_chars_no_spaces(sentence)
    assert result == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Frodo", "odorF"),
        ("Sam", "maS"),
        ("", ""),
        ("A", "A"),
    ],
)
def test_reverse_name(name, expected):
    result = reverse_name(name)
    assert result == expected
