# can_enter_shire
MIN_AGE = 18
WELCOME_MESSAGE = "Welcome to the Shire!"
TOO_YOUNG_MESSAGE = "You are too young!"

# classify_ring_bearer
RING_BEARER = "Frodo"
FORMER_RING_BEARER = "Gollum"
RING_BEARER_MESSAGE = "Ring Bearer"
FORMER_RING_BEARER_MESSAGE = "Former Ring Bearer"
NOT_RING_BEARER_MESSAGE = "Not a Ring Bearer"

# can_join_fellowship
MIN_FELLOWSHIP_AGE = 18
VALID_RACES = ["hobbit", "human", "elf", "dwarf"]

# is_valid_hobbit
MIN_HOBBIT_AGE = 1
MAX_HOBBIT_AGE = 130

# get_quest_status — już masz
READY_THRESHOLD = 80
INJURED_THRESHOLD = 50
CRITICAL_THRESHOLD = 0
READY_MESSAGE = "Ready for quest"
INJURED_MESSAGE = "Injured but can continue"
CRITICAL_MESSAGE = "Critically injured"
DEAD_MESSAGE = "Dead"


def can_enter_shire(age: int) -> str:
    """Returns welcome message if age >= 18, otherwise returns rejection message.
    Example: can_enter_shire(20) -> 'Welcome to the Shire!'
             can_enter_shire(15) -> 'You are too young!'
    """
    if age >= MIN_AGE:
        return WELCOME_MESSAGE
    return TOO_YOUNG_MESSAGE


def classify_ring_bearer(name: str) -> str:
    """Classifies a character based on their relationship with the One Ring.
    Example: classify_ring_bearer('Frodo') -> 'Ring Bearer'
             classify_ring_bearer('Gollum') -> 'Former Ring Bearer'
             classify_ring_bearer('Gandalf') -> 'Not a Ring Bearer'
    """
    if name == RING_BEARER:
        return RING_BEARER_MESSAGE
    if name == FORMER_RING_BEARER:
        return FORMER_RING_BEARER_MESSAGE
    return NOT_RING_BEARER_MESSAGE


def can_join_fellowship(age: int, race: str) -> bool:
    """Returns True if the character is old enough and of a valid race to join the Fellowship.
    Valid races: hobbit, human, elf, dwarf.
    Example: can_join_fellowship(33, 'hobbit') -> True
             can_join_fellowship(15, 'hobbit') -> False
             can_join_fellowship(33, 'orc') -> False
    """
    if age >= MIN_FELLOWSHIP_AGE and race in VALID_RACES:
        return True
    return False


def get_quest_status(health: int) -> str:
    """Returns quest status based on health points.
    health > 80  -> 'Ready for quest'
    health > 50  -> 'Injured but can continue'
    health > 0   -> 'Critically injured'
    health <= 0  -> 'Dead'
    Example: get_quest_status(90) -> 'Ready for quest'
             get_quest_status(30) -> 'Critically injured'
    """
    if health > READY_THRESHOLD:
        return READY_MESSAGE
    if health > INJURED_THRESHOLD:
        return INJURED_MESSAGE
    if health > CRITICAL_THRESHOLD:
        return CRITICAL_MESSAGE
    return DEAD_MESSAGE


def is_valid_hobbit(name: str, age: int) -> bool:
    """Returns True if the hobbit name and age are valid.
    Valid name: starts with uppercase, contains only letters.
    Valid age: between 1 and 130.
    Example: is_valid_hobbit('Frodo', 33) -> True
             is_valid_hobbit('frodo', 33) -> False
             is_valid_hobbit('Frodo', 150) -> False
    """
    if not name:
        return False
    if not name.isalpha():
        return False
    if not name[0].isupper():
        return False
    if age < MIN_HOBBIT_AGE or age > MAX_HOBBIT_AGE:
        return False
    return True