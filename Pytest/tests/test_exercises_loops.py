import pytest
from exercises.exercises_loops import (
    count_fellowship_members,
    find_ring_bearer,
    skip_orcs,
    get_long_names,
    enumerate_fellowship,
    get_uppercase_names,
    get_hobbits,
    get_name_lengths,
    get_short_names,
    flatten_fellowship,
    count_down,
    find_first_orc,
    pair_names_and_races,
    compare_power_levels,
    FOUND_MESSAGE,
    NOT_FOUND_MESSAGE,
    NO_ORCS_MESSAGE,
    HERO_WINS_MESSAGE,
    DRAW_MESSAGE,
    VILLAINS_WINS_MESSAGE,
)


class TestCountFellowshipMembers:
    def test_count_fellowship_members(self, fellowship):
        assert count_fellowship_members(fellowship) == 5

    def test_count_fellowship_members_pairs(self, pairs):
        assert count_fellowship_members(pairs) == 3

    def test_count_fellowship_members_returns_int(self, fellowship):
        result = count_fellowship_members(fellowship)
        assert isinstance(result, int)

    def test_count_missing_fellowship_members(self):
        with pytest.raises(TypeError):
            count_fellowship_members()


class TestFindRingBearer:
    @pytest.mark.parametrize(
        "characters, expected",
        [
            (["Frodo", "Sam", "Gandalf"], FOUND_MESSAGE),
            (["Sam", "Gandalf", "Aragorn"], NOT_FOUND_MESSAGE),
            (["Sam", "Frodo", "Gandalf"], FOUND_MESSAGE),
        ],
    )
    def test_find_ring_bearer(self, characters, expected):
        result = find_ring_bearer(characters)
        assert result == expected

    def test_find_ring_bearer_returns_string(self, fellowship):
        result = find_ring_bearer(fellowship)
        assert isinstance(result, str)


def test_skip_orcs(characters_list, orcs):
    result = skip_orcs(characters_list, orcs)
    assert all(orc not in result for orc in orcs)


def test_get_long_names_all_elements_longer_than_min_length(fellowship):
    min_length = 4
    result = get_long_names(fellowship, min_length)
    assert all(len(name) > min_length for name in result)


class TestEnumerateFellowship:
    def test_enumerate_fellowship_returns_list(self, fellowship):
        result = enumerate_fellowship(fellowship)
        assert isinstance(result, list)

    def test_enumerate_fellowship_all_elements_are_str(self, fellowship):
        result = enumerate_fellowship(fellowship)
        assert all(isinstance(item, str) for item in result)

    def test_enumerate_fellowship(self, fellowship):
        result = enumerate_fellowship(fellowship)
        assert result[0].startswith("1.")
        for i, (item, name) in enumerate(zip(result, fellowship), start=1):
            assert item == f"{i}. {name}"


def test_get_uppercase_names(fellowship):
    result = get_uppercase_names(fellowship)
    assert all(person.isupper() for person in result)


def test_get_hobbits(fellowship):
    result = get_hobbits(fellowship)
    assert all(hobbit.endswith("o") for hobbit in result)


def test_get_name_lengths_correct_lengths(fellowship):
    result = get_name_lengths(fellowship)
    assert all(result[i] == len(fellowship[i]) for i in range(len(fellowship)))


def test_get_short_names(fellowship):
    max_length = 5
    result = get_short_names(fellowship, max_length)
    assert all(len(name) <= max_length for name in result)


def test_flatten_fellowship(groups):
    result = flatten_fellowship(groups)
    assert len(result) == sum(len(group) for group in groups)
    assert all(name in result for group in groups for name in group)


class TestCountDown:
    def test_count_down_returns_list(self):
        n = 5
        result = count_down(n)
        assert isinstance(result, list)

    def test_count_down(self):
        n = 5
        result = count_down(n)
        assert result[0] == n
        assert result[-1] == 0
        assert len(result) == n + 1
        assert all(result[i] > result[i + 1] for i in range(len(result) - 1))


@pytest.mark.parametrize(
    "characters, orcs, expected",
    [
        (["Frodo", "Azog", "Sam"], ["Azog", "Bolg"], "Azog"),
        (["Frodo", "Sam"], ["Azog", "Bolg"], NO_ORCS_MESSAGE),
        (["Frodo", "Bolg", "Azog"], ["Azog", "Bolg"], "Bolg"),
    ],
)
def test_find_first_orc(characters, orcs, expected):
    result = find_first_orc(characters, orcs)
    assert result == expected


def test_pair_names_and_races(fellowship, races):
    result = pair_names_and_races(fellowship, races)
    assert len(result) == len(fellowship)
    assert all(
        f"{name} is a {race}" == item
        for item, name, race in zip(result, fellowship, races)
    )


@pytest.mark.parametrize(
    "heroes, villains, expected",
    [
        (
            [10, 5, 8],
            [7, 9, 8],
            [HERO_WINS_MESSAGE, VILLAINS_WINS_MESSAGE, DRAW_MESSAGE],
        ),
        (
            [12, 5, 9],
            [12, 6, 7],
            [DRAW_MESSAGE, VILLAINS_WINS_MESSAGE, HERO_WINS_MESSAGE],
        ),
    ],
)
def test_compare_power_levels(heroes, villains, expected):
    result = compare_power_levels(heroes, villains)
    assert result == expected