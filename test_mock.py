import pytest
import mock as mt3

# ------------------------
# Question 1 – Nested Sum
# ------------------------
def test_nested_sum_basic():
    assert mt3.nested_sum([1,2,3]) == 6
    assert mt3.nested_sum([1,[2,3],[4,[5]]]) == 15
    assert mt3.nested_sum([]) == 0
    assert mt3.nested_sum([[[]]]) == 0

# ------------------------
# Question 2 – Reverse Dictionary
# ------------------------
def test_reverse_dict_basic():
    d = {'a':1,'b':2,'c':1}
    assert mt3.reverse_dict(d) == {1:['a','c'],2:['b']}

# ------------------------
# Question 3 – Fibonacci Check
# ------------------------
def test_is_fibonacci():
    fib_nums = [0,1,1,2,3,5,8,13,21]
    for n in fib_nums:
        assert mt3.is_fibonacci(n) == True
    for n in [4,6,7,9,10,14]:
        assert mt3.is_fibonacci(n) == False

# ------------------------
# Question 4 – Deep Flatten
# ------------------------
def test_deep_flatten():
    assert mt3.deep_flatten([1, [2, [3, 4], 5], 6]) == [1,2,3,4,5,6]
    assert mt3.deep_flatten([]) == []
    assert mt3.deep_flatten([[[[1]]]]) == [1]

# ------------------------
# Question 5 – Pyramid Pattern
# ------------------------
def test_pyramid_pattern(capsys):
    mt3.pyramid_pattern("ABC")
    captured = capsys.readouterr().out
    assert captured.strip() == "A\nAB\nABC"

# ------------------------
# Question 6 – Max Consecutive Duplicate
# ------------------------
def test_max_consecutive():
    assert mt3.max_consecutive([1,1,2,2,2,3]) == 3
    assert mt3.max_consecutive([]) == 0
    assert mt3.max_consecutive(['a','a','a','b','b']) == 3

# ------------------------
# Question 7 – Dictionary Filter
# ------------------------
def test_filter_dict():
    d = {'a':5,'b':3,'c':10}
    assert mt3.filter_dict(d, 5) == {'a':5,'c':10}
    assert mt3.filter_dict(d, 11) == {}

# ------------------------
# Question 8 – Nested Max Depth
# ------------------------
def test_max_depth():
    assert mt3.max_depth([1, [2,3], [4, [5]]]) == 3
    assert mt3.max_depth([]) == 1
    assert mt3.max_depth([[[[]]]]) == 4

# ------------------------
# Question 9 – Recursive String Reverser
# ------------------------
def test_reverse_words_rec():
    assert mt3.reverse_words_rec("This is a test") == "test a is This"
    assert mt3.reverse_words_rec("Python") == "Python"
    assert mt3.reverse_words_rec("") == ""

# ------------------------
# Question 10 – Column Sum
# ------------------------
def test_column_sum():
    assert mt3.column_sum([[1,2,3],[4,5,6],[7,8,9]]) == [12,15,18]
    assert mt3.column_sum([]) == []
    assert mt3.column_sum([[1]]) == [1]