import pytest
from find_dup_strs.find_dup_strs import find_duplicate_positions

def test_no_duplicates_1():
    strings = ["a", "b", "c", "d"]
    expected = []
    assert find_duplicate_positions(strings) == expected

def test_single_duplicate_2():
    strings = ["dup_a", "b", "dup_a"]
    expected = [["dup_a", 0, 2]]
    assert find_duplicate_positions(strings) == expected

def test_multiple_duplicates_3():
    strings = ["dup_a", "dup_b", "dup_a", "c", "dup_b"]
    expected = [["dup_a", 0, 2], ["dup_b", 1, 4]]
    assert find_duplicate_positions(strings) == expected

def test_all_duplicates_4():
    strings = ["dup_a", "dup_a", "dup_a", "dup_a"]
    expected = [["dup_a", 0, 1, 2, 3]]
    assert find_duplicate_positions(strings) == expected

def test_empty_list_5():
    strings = []
    expected = []
    assert find_duplicate_positions(strings) == expected

def test_no_strings_6():
    strings = [""]
    expected = []
    assert find_duplicate_positions(strings) == expected

def test_mixed_case_duplicates_7():
    strings = ["dup_a", "dup_A", "dup_a", "dup_A"]
    expected = [["dup_a", 0, 2], ["dup_A", 1, 3]]
    assert find_duplicate_positions(strings) == expected

def test_three_duplicates_8():
    strings = ["dup_a", "dup_b", "dup_a", "dup_c", "dup_b", "dup_a"]
    expected = [["dup_a", 0, 2, 5], ["dup_b", 1, 4]]
    assert find_duplicate_positions(strings) == expected

def test_four_duplicates_9():
    strings = ["dup_a", "dup_b", "dup_a", "dup_c", "dup_b", "dup_a", "dup_c", "dup_a"]
    expected = [["dup_a", 0, 2, 5, 7], ["dup_b", 1, 4], ["dup_c", 3, 6]]
    assert find_duplicate_positions(strings) == expected

if __name__ == "__main__":
    pytest.main()