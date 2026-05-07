import pytest
from exercises.exercises_lists import (
    get_first,
    get_last,
    count_members,
    remove_member,
    add_member,
    sort_fellowship,
    is_member,
    reverse_fellowship,
    merge_fellowships,
    remove_duplicates,
)

class TestGetFirst:
    def test_get_first(self, fellowship):
        assert get_first(fellowship) == "Frodo"

    def test_get_first_empty_list(self):
        with pytest.raises(IndexError):
            get_first([])


class TestGetLast:
    def test_get_last(self, fellowship):
        assert get_last(fellowship) == "Legolas"

    def test_get_last_empty_list(self):
        with pytest.raises(IndexError):
            get_last([])

def test_count_members(fellowship):
    assert count_members(fellowship) == 5


def test_add_member(fellowship):
    result = add_member(fellowship, "Boromir")
    assert "Boromir" in result
    assert result[-1] == "Boromir"
    assert count_members(result) == 6


class TestRemoveMember:
    def test_remove_member(self, fellowship):
        result = remove_member(fellowship, "Aragorn")
        assert "Aragorn" not in result
        assert count_members(result) == 4

    def test_remove_member_not_in_list(self, fellowship):
        with pytest.raises(ValueError):
            remove_member(fellowship, "Sauron")


def test_sort_fellowship(fellowship):
    result = sort_fellowship(fellowship)
    assert result == sorted(fellowship)


def test_sort_fellowship_does_not_modify_original(fellowship):
    original = fellowship.copy()
    sort_fellowship(fellowship)
    assert fellowship == original


class TestIsMember:
    def test_is_member_true(self, fellowship):
        assert is_member(fellowship, "Frodo") is True

    def test_is_member_false(self, fellowship):
        assert is_member(fellowship, "Sauron") is False

    def test_is_member_empty_list(self):
        assert is_member([], "Frodo") is False


class TestReverseFellowship:
    def test_reverse_fellowship(self, fellowship):
        result = reverse_fellowship(fellowship)
        assert result == ["Legolas", "Aragorn", "Gandalf", "Sam", "Frodo"]

    def test_reverse_fellowship_does_not_modify_original(self, fellowship):
        original = fellowship.copy()
        reverse_fellowship(fellowship)
        assert fellowship == original


class TestMerge:
    def test_merge_fellowships(self, fellowship):
        hobbits = ["Pippin", "Merry"]
        result = merge_fellowships(fellowship, hobbits)
        assert result == ["Frodo", "Sam", "Gandalf", "Aragorn", "Legolas", "Pippin", "Merry"]
        assert count_members(result) == 7

    def test_merge_fellowships_with_empty(self, fellowship):
        result = merge_fellowships(fellowship, [])
        assert result == fellowship


class TestRemoveDuplicates:
    def test_remove_duplicates(self):
        duplicates = ["Frodo", "Sam", "Frodo", "Gandalf", "Sam"]
        result = remove_duplicates(duplicates)
        assert result == ["Frodo", "Sam", "Gandalf"]

    def test_remove_duplicates_no_duplicates(self, fellowship):
        result = remove_duplicates(fellowship)
        assert result == fellowship

    def test_remove_duplicates_preserves_order(self):
        duplicates = ["Sam", "Frodo", "Sam"]
        result = remove_duplicates(duplicates)
        assert result[0] == "Sam"
        assert result[1] == "Frodo"

    def test_remove_duplicates_empty_list(self):
        assert remove_duplicates([]) == []