import pytest


@pytest.fixture
def fellowship():
    return ["Frodo", "Sam", "Gandalf", "Aragorn", "Legolas"]


@pytest.fixture
def characters():
    return {
        "Frodo": "hobbit",
        "Gandalf": "wizard",
        "Aragorn": "human",
        "Legolas": "elf",
        "Gimli": "dwarf",
    }


@pytest.fixture
def coordinates():
    return (1, 2, 3, 4, 5, 3, 2, 5, 5)


@pytest.fixture
def person():
    return ("Frodo", 33, "Shire", "hobbit")


@pytest.fixture
def workers():
    return (
        ("Frodo", 5000),
        ("Sam", 3000),
        ("Gandalf", 8000),
        ("Pippin", 2000),
        ("Aragorn", 6000),
    )


@pytest.fixture
def enemies():
    return {"Sauron", "Saruman", "Nazgul", "Shelob", "Balrog"}


@pytest.fixture
def gondors_enemies():
    return {"Sauron", "Nazgul", "Corsairs", "Haradrim"}


@pytest.fixture
def races():
    return ["hobbit", "hobbit", "wizard", "human", "elf"]


@pytest.fixture
def pairs():
    return [("Frodo", "hobbit"), ("Gandalf", "wizard"), ("Aragorn", "human")]


@pytest.fixture
def groups():
    return [
        ["Frodo", "Sam", "Pippin", "Merry"],
        ["Gandalf", "Aragorn", "Boromir"],
        ["Legolas", "Gimli"],
    ]
