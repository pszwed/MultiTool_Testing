from typing import Any
from collections import Counter, defaultdict, OrderedDict, deque

# Dictionaries


def get_character(characters: dict[str, str], name: str) -> str:
    """Returns the race of a character. Example: get_character({'Frodo': 'hobbit'}, 'Frodo') -> 'hobbit'"""
    return characters[name]


def add_character(characters: dict[str, str], name: str, race: str) -> dict[str, str]:
    """Adds a new character to the dictionary and returns it. Example: add_character({'Frodo': 'hobbit'}, 'Gandalf', 'wizard') -> {'Frodo': 'hobbit', 'Gandalf': 'wizard'}"""
    characters[name] = race
    return characters


def get_all_names(characters: dict[str, str]) -> list[str]:
    """Returns a list of all character names. Example: get_all_names({'Frodo': 'hobbit', 'Gandalf': 'wizard'}) -> ['Frodo', 'Gandalf']"""
    return list(characters.keys())


def is_character(characters: dict[str, str], name: str) -> bool:
    """Returns True if the character exists in the dictionary. Example: is_character({'Frodo': 'hobbit'}, 'Sauron') -> False"""
    return name in characters


# Tuples


def get_first(coordinates: tuple) -> Any:
    """Returns the first element of a tuple. Example: get_first((1, 2, 3)) -> 1"""
    return coordinates[0]


def get_length(coordinates: tuple) -> int:
    """Returns the length of a tuple. Example: get_length((1, 2, 3)) -> 3"""
    return len(coordinates)


def count_in_tuple(coordinates: tuple, value: Any) -> int:
    """Counts occurrences of a value in a tuple. Example: count_in_tuple((1, 2, 2, 3), 2) -> 2"""
    return coordinates.count(value)


def repacked_tuple(person: tuple[str, int, str, str]) -> str:
    """Unpacks a tuple and returns a formatted string. Example: repacked_tuple(('Frodo', 33, 'Shire', 'hobbit')) -> 'Name: Frodo, Age: 33, City: Shire, Profession: hobbit'"""
    name, age, city, profession = person
    return f"Name: {name}, Age: {age}, City: {city}, Profession: {profession}"


def filter_tuple(workers: tuple[tuple[str, int], ...]) -> list[str]:
    """Returns a list of workers earning more than 4000. Example: filter_tuple((('Frodo', 5000), ('Sam', 3000))) -> ['Frodo: 5000']"""
    result = []
    for name, salary in workers:
        if salary > 4000:
            result.append(f"{name}: {salary}")
    return result


# Sets


def add_to_set(enemies: set[str], name: str) -> set[str]:
    """Adds an enemy to the set and returns it. Example: add_to_set({'Sauron', 'Saruman'}, 'Balrog') -> {'Sauron', 'Saruman', 'Balrog'}"""
    enemies.add(name)
    return enemies


def remove_from_set(enemies: set[str], name: str) -> set[str]:
    """Removes an enemy from the set and returns it. Example: remove_from_set({'Sauron', 'Saruman'}, 'Saruman') -> {'Sauron'}"""
    enemies.remove(name)
    return enemies


def is_in_set(enemies: set[str], name: str) -> bool:
    """Returns True if the enemy is in the set. Example: is_in_set({'Sauron', 'Saruman'}, 'Sauron') -> True"""
    return name in enemies


def union_enemies(enemies: set[str], gondors_enemies: set[str]) -> set[str]:
    """Returns all enemies from both sets. Example: union_enemies({'Sauron', 'Saruman'}, {'Nazgul'}) -> {'Sauron', 'Saruman', 'Nazgul'}"""
    return enemies.union(gondors_enemies)


def common_enemies(enemies: set[str], gondors_enemies: set[str]) -> set[str]:
    """Returns enemies common to both sets. Example: common_enemies({'Sauron', 'Saruman'}, {'Sauron', 'Nazgul'}) -> {'Sauron'}"""
    return enemies & gondors_enemies


def unique_enemies(enemies: set[str], gondors_enemies: set[str]) -> set[str]:
    """Returns enemies that belong to only one of the sets. Example: unique_enemies({'Sauron', 'Saruman'}, {'Sauron', 'Nazgul'}) -> {'Saruman', 'Nazgul'}"""
    return enemies ^ gondors_enemies


def not_common_enemies(enemies: set[str], gondors_enemies: set[str]) -> set[str]:
    """Returns enemies that belong only to the first set. Example: not_common_enemies({'Sauron', 'Saruman'}, {'Sauron', 'Nazgul'}) -> {'Saruman'}"""
    return enemies - gondors_enemies


# Collections


def count_races(characters: list[str]) -> Counter:
    """Counts occurrences of each race. Example: count_races(['hobbit', 'wizard', 'hobbit']) -> Counter({'hobbit': 2, 'wizard': 1})"""
    return Counter(characters)


def most_common_race(characters: list[str]) -> str:
    """Returns the most common race. Example: most_common_race(['hobbit', 'wizard', 'hobbit']) -> 'hobbit'"""
    return Counter(characters).most_common(1)[0][0]


def create_ordered(pairs: list[tuple[str, str]]) -> OrderedDict:
    """Creates an OrderedDict from a list of pairs preserving order. Example: create_ordered([('Frodo', 'hobbit'), ('Sam', 'hobbit')]) -> OrderedDict([('Frodo', 'hobbit'), ('Sam', 'hobbit')])"""
    return OrderedDict(pairs)


def create_deque(characters: list[str], name: str) -> deque:
    """Adds a member to the front of a deque and returns it. Example: create_deque(['Sam', 'Gandalf'], 'Frodo') -> deque(['Frodo', 'Sam', 'Gandalf'])"""
    d = deque(characters)
    d.appendleft(name)
    return d
