import pytest
from exercises.isinstance_demo import show_type


@pytest.mark.parametrize(
    "value, expected",
    [
        # int:
        (1, "Number: 2"),
        (0, "Number: 0"),
        (-3, "Number: -6"),
        # float:
        (1.0, "Number: 2.0"),
        (3.2, "Number: 6.4"),
        (-5.1, "Number: -10.2"),
    ],
)
def test_show_type_with_numbers(value, expected):
    assert show_type(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("butter", "String: BUTTER"),
        ("", "String: "),
        ("123", "String: 123"),
    ],
)
def test_show_type_with_strings(value, expected):
    assert show_type(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ([1, 2, 3, 4, 5], "List has 5 elements"),
        ([], "List has 0 elements"),
        ([1], "List has 1 elements"),
    ],
)
def test_show_type_with_lists(value, expected):
    assert show_type(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (True, "Bool: True"),
        (False, "Bool: False"),
    ],
)
def test_show_type_with_bool(value, expected):
    assert show_type(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        {"a": 1},
        (1, 2),
        None,
    ],
)
def test_show_type_returns_none_for_unsupported_types(value):
    assert show_type(value) is None
