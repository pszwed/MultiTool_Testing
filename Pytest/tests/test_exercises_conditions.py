import pytest
from exercises.exercises_conditions import (
    can_enter_shire,
    classify_ring_bearer,
    can_join_fellowship,
    get_quest_status,
    is_valid_hobbit,
    MIN_AGE,
    WELCOME_MESSAGE,
    TOO_YOUNG_MESSAGE,
    RING_BEARER,
    FORMER_RING_BEARER,
    RING_BEARER_MESSAGE,
    FORMER_RING_BEARER_MESSAGE,
    NOT_RING_BEARER_MESSAGE,
    MIN_FELLOWSHIP_AGE,
    VALID_RACES,
    MIN_HOBBIT_AGE,
    MAX_HOBBIT_AGE,
    READY_THRESHOLD,
    INJURED_THRESHOLD,
    CRITICAL_THRESHOLD,
    READY_MESSAGE,
    INJURED_MESSAGE,
    CRITICAL_MESSAGE,
    DEAD_MESSAGE,
)


class TestCanEnterShire:
    @pytest.mark.parametrize("age", [MIN_HOBBIT_AGE, MIN_AGE + 1])
    def test_can_enter_shire_returns_string(self, age):
        result = can_enter_shire(age)
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        "age, expected",
        [
            (MIN_AGE - 18, TOO_YOUNG_MESSAGE),
            (MIN_AGE - 1, TOO_YOUNG_MESSAGE),
            (MIN_AGE, WELCOME_MESSAGE),
            (MIN_AGE + 1, WELCOME_MESSAGE),
            (MAX_HOBBIT_AGE, WELCOME_MESSAGE),
        ],
    )
    def test_can_enter_shire(self, age, expected):
        result = can_enter_shire(age)
        assert result == expected

    def test_can_enter_shire_wrong_age_type(self):
        age = str(MIN_AGE)
        with pytest.raises(TypeError):
            can_enter_shire(age)

    def test_can_enter_shire_missing_age(self):
        with pytest.raises(TypeError):
            can_enter_shire()


class TestClassifyRingBearer:
    @pytest.mark.parametrize("bearer", [RING_BEARER, FORMER_RING_BEARER, "Gandalf"])
    def test_classify_ring_bearer_returns_string(self, bearer):
        result = classify_ring_bearer(bearer)
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        "bearer, message",
        [
            (RING_BEARER, RING_BEARER_MESSAGE),
            (FORMER_RING_BEARER, FORMER_RING_BEARER_MESSAGE),
            ("Gandalf", NOT_RING_BEARER_MESSAGE),
        ],
    )
    def test_classify_ring_bearer(self, bearer, message):
        result = classify_ring_bearer(bearer)
        assert result == message

    def test_classify_ring_bearer_missing_bearer(self):
        with pytest.raises(TypeError):
            classify_ring_bearer()


class TestCanJoinFellowship:
    @pytest.mark.parametrize(
        "age, race", [(MIN_FELLOWSHIP_AGE - 1, "hobbit"), (MIN_FELLOWSHIP_AGE, "human")]
    )
    def test_can_join_fellowship_returns_bool(self, age, race):
        result = can_join_fellowship(age, race)
        assert isinstance(result, bool)

    @pytest.mark.parametrize(
        "age, race, expected",
        [
            (MIN_FELLOWSHIP_AGE - 1, "hobbit", False),
            (MIN_FELLOWSHIP_AGE, "human", True),
            (MIN_FELLOWSHIP_AGE + 1, "elf", True),
            (MIN_FELLOWSHIP_AGE - 1, "orc", False),
            (MIN_FELLOWSHIP_AGE, "orc", False),
            (MIN_FELLOWSHIP_AGE + 1, "orc", False),
        ],
    )
    def test_can_join_fellowship(self, age, race, expected):
        result = can_join_fellowship(age, race)
        assert result == expected

    def test_can_join_fellowship_missing_parameters(self):
        with pytest.raises(TypeError):
            can_join_fellowship()

    def test_can_join_fellowship_wrong_age_type(self):
        with pytest.raises(TypeError):
            can_join_fellowship(str(MIN_FELLOWSHIP_AGE), "hobbit")

    @pytest.mark.parametrize("race", VALID_RACES)
    def test_can_join_fellowship_valid_races(self, race):
        result = can_join_fellowship(MIN_FELLOWSHIP_AGE, race)
        assert result is True


class TestGetQuestStatus:
    def test_get_quest_status_returns_string(self):
        result = get_quest_status(READY_THRESHOLD)
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        "health, expected",
        [
            (READY_THRESHOLD + 1, READY_MESSAGE),
            (READY_THRESHOLD, INJURED_MESSAGE),
            (INJURED_THRESHOLD + 1, INJURED_MESSAGE),
            (INJURED_THRESHOLD, CRITICAL_MESSAGE),
            (CRITICAL_THRESHOLD + 1, CRITICAL_MESSAGE),
            (CRITICAL_THRESHOLD, DEAD_MESSAGE),
            (-10, DEAD_MESSAGE),
        ],
    )
    def test_get_quest_status(self, health, expected):
        result = get_quest_status(health)
        assert result == expected

    def test_get_quest_status_wrong_health_value_type(self):
        health = str(READY_THRESHOLD)
        with pytest.raises(TypeError):
            get_quest_status(health)

    def test_get_quest_status_missing_health(self):
        with pytest.raises(TypeError):
            get_quest_status()


class TestIsValidHobbit:
    def test_is_valid_hobbit_returns_bool(self):
        name = "Frodo"
        result = is_valid_hobbit(name, MIN_HOBBIT_AGE)
        assert isinstance(result, bool)

    @pytest.mark.parametrize(
        "name, age, expected",
        [
            ("Frodo", MIN_HOBBIT_AGE - 1, False),
            ("Frodo", MIN_HOBBIT_AGE, True),
            ("Frodo", MIN_HOBBIT_AGE + 1, True),
            ("Frodo", MAX_HOBBIT_AGE - 1, True),
            ("Frodo", MAX_HOBBIT_AGE, True),
            ("Frodo", MAX_HOBBIT_AGE + 1, False),
            ("frodo", MIN_HOBBIT_AGE, False),
            ("Frodo2", MIN_HOBBIT_AGE, False),
            ("", MIN_HOBBIT_AGE, False),
        ],
    )
    def test_is_valid_hobbit(self, name, age, expected):
        result = is_valid_hobbit(name, age)
        assert result == expected
