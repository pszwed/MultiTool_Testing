import pytest
from collections import Counter, OrderedDict, deque
from exercises.exercises_data_structures import (
    get_character,
    add_character,
    get_all_names,
    is_character,
    get_first,
    get_length,
    count_in_tuple,
    repacked_tuple,
    filter_tuple,
    add_to_set,
    remove_from_set,
    is_in_set,
    union_enemies,
    common_enemies,
    unique_enemies,
    not_common_enemies,
    count_races,
    most_common_race,
    create_ordered,
    create_deque,
)


class TestGetCharacter:
    def test_get_frodo(self, characters):
        name = "Frodo"
        result = get_character(characters, name)
        assert result == "hobbit"

    def test_get_gandalf(self, characters):
        name = "Gandalf"
        result = get_character(characters, name)
        assert result == "wizard"

    def test_get_missing_key(self, characters):
        name = "Sauron"
        with pytest.raises(KeyError):
            get_character(characters, name)


class TestAddCharacter:
    def test_add_boromir(self, characters):
        name = "Boromir"
        race = "human"
        result = add_character(characters, name, race)
        assert name in result
        assert result[name] == race

    def test_add_missing_race(self, characters):
        name = "Gollum"
        with pytest.raises(TypeError):
            add_character(characters, name)

    def test_add_increases_count(self, characters):
        count = len(characters)
        result = add_character(characters, "Boromir", "human")
        assert len(result) > count


def test_get_all_names(characters):
    result = get_all_names(characters)
    assert isinstance(result, list)
    assert "Frodo" in result


class TestIsCharacter:
    def test_is_character_true(self, characters):
        name = "Frodo"
        result = is_character(characters, name)
        assert result is True

    def test_is_character_false(self, characters):
        name = "Sauron"
        result = is_character(characters, name)
        assert result is False


class TestGetFirst:
    @pytest.mark.parametrize(
        "coordinates, expected",
        [
            ((1, 2, 3), 1),
            ((9, 8, 7), 9),
        ],
    )
    def test_get_first(self, coordinates, expected):
        result = get_first(coordinates)
        assert result == expected

    def test_get_first_empty(self):
        with pytest.raises(IndexError):
            get_first(())


@pytest.mark.parametrize(
    "coordinates, expected",
    [
        ((1, 2, 3, 4, 5, 3, 2, 5, 5), 9),
        ((), 0),
        ((1,), 1),
    ],
)
def test_get_length(coordinates, expected):
    result = get_length(coordinates)
    assert result == expected


def test_count_in_tuple(coordinates):
    value = 5
    expected = 3
    result = count_in_tuple(coordinates, value)
    assert result == expected


class TestRepackedTuple:
    def test_repacked_tuple(self, person):
        expected = "Name: Frodo, Age: 33, City: Shire, Profession: hobbit"
        result = repacked_tuple(person)
        assert result == expected

    def test_repacked_tuple_returns_string(self, person):
        result = repacked_tuple(person)
        assert isinstance(result, str)

    def test_repacked_tuple_contains_name(self, person):
        name = "Frodo"
        result = repacked_tuple(person)
        assert name in result


class TestFilterTuple:
    def test_filter_tuple(self, workers):
        result = filter_tuple(workers)
        assert "Frodo: 5000" in result
        assert "Gandalf: 8000" in result
        assert "Aragorn: 6000" in result
        assert "Sam: 3000" not in result
        assert "Pippin: 2000" not in result

    def test_filter_tuple_nobody_qualifies(self):
        poor_workers = (("Sam", 0), ("Pippin", 4000))
        result = filter_tuple(poor_workers)
        assert result == []

    def test_filter_tuple_all_qualify(self):
        rich_workers = (("Gandalf", 9000), ("Aragorn", 8000))
        result = filter_tuple(rich_workers)
        assert len(result) == 2

    def test_filter_tuple_returns_list(self, workers):
        result = filter_tuple(workers)
        assert isinstance(result, list)


class TestAddToSet:
    def test_add_to_set(self, enemies):
        name = "Gollum"
        result = add_to_set(enemies, name)
        assert name in result
        assert isinstance(result, set)

    def test_add_to_set_missing_arg(self):
        with pytest.raises(TypeError):
            add_to_set(123)

    def test_add_increases_size(self, enemies):
        name = "Gollum"
        count = len(enemies)
        result = add_to_set(enemies, name)
        assert len(result) > count

    def test_add_existing_member(self, enemies):
        name = "Sauron"
        count = len(enemies)
        result = add_to_set(enemies, name)
        assert len(result) == count


class TestRemoveFromSet:
    def test_remove_from_set(self, enemies):
        name = "Sauron"
        result = remove_from_set(enemies, name)
        assert name not in result

    def test_remove_from_set_not_in_set(self, enemies):
        with pytest.raises(KeyError):
            remove_from_set(enemies, "Gollum")


@pytest.mark.parametrize("name, expected", [("Saruman", True), ("Gollum", False)])
def test_is_in_set(enemies, name, expected):
    result = is_in_set(enemies, name)
    assert result == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Haradrim", True),
        ("Shelob", True),
        ("Sauron", True),
        ("Gollum", False),
    ],
)
def test_union_enemies(enemies, gondors_enemies, name, expected):
    result = union_enemies(enemies, gondors_enemies)
    assert (name in result) == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Sauron", True),
        ("Nazgul", True),
        ("Shelob", False),
        ("Haradrim", False),
    ],
)
def test_common_enemies(enemies, gondors_enemies, name, expected):
    result = common_enemies(enemies, gondors_enemies)
    assert (name in result) == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Shelob", True),
        ("Sauron", False),
        ("Haradrim", True),
    ],
)
def test_unique_enemies(enemies, gondors_enemies, name, expected):
    result = unique_enemies(enemies, gondors_enemies)
    assert (name in result) == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Shelob", True),
        ("Saruman", True),
        ("Haradrim", False),
    ],
)
def test_not_common_enemies(enemies, gondors_enemies, name, expected):
    result = not_common_enemies(enemies, gondors_enemies)
    assert (name in result) == expected


class TestCountRaces:
    def test_count_races(self, races):
        result = count_races(races)
        assert result["hobbit"] == 2
        assert result["wizard"] == 1
        assert result["elf"] == 1
        assert isinstance(result, Counter)

    def test_count_races_empty(self):
        result = count_races([])
        assert result == Counter()


def test_most_common_race(races):
    result = most_common_race(races)
    assert result == "hobbit"
    assert isinstance(result, str)


class TestCreateOrdered:
    def test_create_ordered(self, pairs):
        result = create_ordered(pairs)
        assert isinstance(result, OrderedDict)
        assert list(result.keys()) == ["Frodo", "Gandalf", "Aragorn"]
        assert list(result.values()) == ["hobbit", "wizard", "human"]

    def test_create_ordered_empty(self):
        result = create_ordered([])
        assert result == OrderedDict()
        assert isinstance(result, OrderedDict)


class TestCreateDeque:
    def test_create_deque_returns_deque(self, fellowship):
        name = "Gimli"
        result = create_deque(fellowship, name)
        assert isinstance(result, deque)

    def test_create_deque_name_is_first(self, fellowship):
        name = "Gimli"
        result = create_deque(fellowship, name)
        assert result[0] == name

    def test_create_deque_increases_size(self, fellowship):
        name = "Gimli"
        count = len(fellowship)
        result = create_deque(fellowship, name)
        assert len(result) == count + 1

    def test_create_deque_empty_list(self):
        name = "Frodo"
        result = create_deque([], name)
        assert result[0] == name
        assert len(result) == 1

    def test_create_deque_missing_arg(self):
        with pytest.raises(TypeError):
            create_deque([])
