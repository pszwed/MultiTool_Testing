FOUND_MESSAGE = "Found: Frodo"
NOT_FOUND_MESSAGE = "Not Found"
NO_ORCS_MESSAGE = "No orcs found"
HERO_WINS_MESSAGE = "Hero wins"
DRAW_MESSAGE = "Draw"
VILLAINS_WINS_MESSAGE = "Villain wins"


def count_fellowship_members(fellowship: list[str]) -> int:
    """Counts fellowship members using a for loop without len().
    Example: count_fellowship_members(["Frodo", "Sam"]) -> 2
    """
    count = 0
    for person in fellowship:
        count += 1
    return count


def find_ring_bearer(fellowship: list[str]) -> str:
    """Finds first Frodo in the fellowship using for loop and break.
    Example: find_ring_bearer(["Sam", "Frodo"]) -> 'Found: Frodo'
             find_ring_bearer(["Sam", "Gandalf"]) -> 'Not Found'
    """
    for person in fellowship:
        if person == "Frodo":
            return FOUND_MESSAGE
    return NOT_FOUND_MESSAGE


def skip_orcs(characters: list[str], orcs: list[str]) -> list[str]:
    """Returns list of characters skipping orcs using continue.
    Example: skip_orcs(["Frodo", "Azog", "Sam"], ["Azog"]) -> ["Frodo", "Sam"]
    """
    heroes = []
    for person in characters:
        if person in orcs:
            continue
        heroes.append(person)
    return heroes


def get_long_names(fellowship: list[str], min_length: int) -> list[str]:
    """Returns list of names longer than min_length.
    Example: get_long_names(["Frodo", "Sam", "Gandalf"], 4) -> ["Frodo", "Gandalf"]
    """
    characters = []
    for person in fellowship:
        if len(person) > min_length:
            characters.append(person)
    return characters


def enumerate_fellowship(fellowship: list[str]) -> list[str]:
    """Returns list of strings with index and name using enumerate.
    Example: enumerate_fellowship(["Frodo", "Sam"]) -> ["1. Frodo", "2. Sam"]
    """
    characters = []
    for i, person in enumerate(fellowship, start=1):
        characters.append(f"{i}. {person}")
    return characters


def get_uppercase_names(fellowship: list[str]) -> list[str]:
    """Returns list of names in uppercase using list comprehension.
    Example: get_uppercase_names(["Frodo", "Sam"]) -> ["FRODO", "SAM"]
    """
    result = [person.upper() for person in fellowship]
    return result


def get_hobbits(fellowship: list[str]) -> list[str]:
    """Returns list of names ending with 'o' using list comprehension.
    Example: get_hobbits(["Frodo", "Sam", "Bilbo"]) -> ["Frodo", "Bilbo"]
    """
    result = [person for person in fellowship if person.endswith("o")]
    return result


def get_name_lengths(fellowship: list[str]) -> list[int]:
    """Returns list of name lengths using list comprehension.
    Example: get_name_lengths(["Frodo", "Sam"]) -> [5, 3]
    """
    result = [len(person) for person in fellowship]
    return result


def get_short_names(fellowship: list[str], max_length: int) -> list[str]:
    """Returns list of names shorter than or equal to max_length.
    Example: get_short_names(["Frodo", "Sam", "Gandalf"], 4) -> ["Sam"]
    """
    result = [person for person in fellowship if len(person) <= max_length]
    return result


def flatten_fellowship(groups: list[list[str]]) -> list[str]:
    """Flattens a list of lists into a single list using list comprehension.
    Example: flatten_fellowship([["Frodo", "Sam"], ["Gandalf"]]) -> ["Frodo", "Sam", "Gandalf"]
    """
    result = [person for group in groups for person in group]
    return result


def count_down(n: int) -> list[int]:
    """Returns a list counting down from n to 0 using while loop.
    Example: count_down(5) -> [5, 4, 3, 2, 1, 0]
    """
    result = []
    while n >= 0:
        result.append(n)
        n -= 1
    return result


def find_first_orc(characters: list[str], orcs: list[str]) -> str:
    """Finds the first orc in the characters list using a while loop.
    Example: find_first_orc(["Frodo", "Azog", "Sam"], ["Azog", "Bolg"]) -> "Azog"
             find_first_orc(["Frodo", "Sam"], ["Azog", "Bolg"]) -> "No orcs found"
    """
    i = 0
    while i < len(characters):
        if characters[i] in orcs:
            return characters[i]
        i += 1
    return NO_ORCS_MESSAGE


def pair_names_and_races(names: list[str], races: list[str]) -> list[str]:
    """Pairs names and races into formatted strings using zip.
    Example: pair_names_and_races(["Frodo", "Gandalf"], ["hobbit", "wizard"])
             -> ["Frodo is a hobbit", "Gandalf is a wizard"]
    """
    result = []
    for name, race in zip(names, races):
        result.append(f"{name} is a {race}")
    return result


def compare_power_levels(heroes: list[int], villains: list[int]) -> list[str]:
    """Compares power levels of heroes and villains using zip.
    Example: compare_power_levels([10, 5, 8], [7, 9, 8])
             -> ["Hero wins", "Villain wins", "Draw"]
    """
    result = []
    for hero, villain in zip(heroes, villains):
        if hero > villain:
            result.append(HERO_WINS_MESSAGE)
        elif hero == villain:
            result.append(DRAW_MESSAGE)
        else:
            result.append(VILLAINS_WINS_MESSAGE)
    return result
