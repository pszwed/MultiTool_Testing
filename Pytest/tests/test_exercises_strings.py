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
        assert greet(name) == expected

    def test_greet_returns_string(self):
        assert isinstance(greet("Frodo"), str)


@pytest.mark.parametrize(
    "name, expected",
    [("Frodo", "FRODO"), ("Legolas", "LEGOLAS"), ("sauron", "SAURON"), ("", "")],
)
def test_to_uppercase(name, expected):
    assert to_uppercase(name) == expected


class TestIsHobbit:
    def test_frodo_is_hobbit(self):
        assert is_hobbit("Frodo") is True

    def test_bilbo_is_hobbit(self):
        assert is_hobbit("Bilbo") is True

    def test_gandalf_is_not_hobbit(self):
        assert is_hobbit("Gandalf") is False

    def test_empty_string(self):
        assert is_hobbit("") is False


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
        assert get_initials(first_name, last_name) == expected

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
    assert count_letter_o(name) == expected


def test_replace_name():
    assert replace_name("Frodo goes to Mordor", "Frodo", "Sam") == "Sam goes to Mordor"


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("Frodo Baggins hobbit", ["Frodo", "Baggins", "hobbit"]),
        ("Frodo", ["Frodo"]),
        ("Frodo  Sam", ["Frodo", "Sam"]),
    ],
)
def test_split_sentence(sentence, expected):
    assert split_sentence(sentence) == expected


@pytest.mark.parametrize(
    "names, expected",
    [
        (["Frodo", "Sam", "Gandalf"], "Frodo, Sam, Gandalf"),
        (["Frodo"], "Frodo"),
        ([], ""),
    ],
)
def test_join_fellowship(names, expected):
    assert join_fellowship(names) == expected


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
    assert is_letters_only(name) == expected


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
    assert is_capitalized(name) == expected


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
    assert count_chars_no_spaces(sentence) == expected


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
    assert reverse_name(name) == expected
