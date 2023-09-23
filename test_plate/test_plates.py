import pytest
from plate import is_valid


def test_input(): # test if the input is a string
    with pytest.raises(TypeError):
        is_valid(2)


def test_max_min_char(): # test if the plate has the right size
    assert is_valid("t") == False
    assert is_valid("trewqyu") == False


def test_begining(): # test if the first 2 char are letters
    assert is_valid("34gdfg") == False
    assert is_valid("r.ythe4") == False


def test_number_end(): # test if the numbers are at the end
    assert is_valid("grt078") == False
    assert is_valid("gre7u7") == False
    assert is_valid("gret54") == True


def test_ponctuation(): # test if there is any period, space or pontcuation
    assert is_valid("ghn.ei") == False
    assert is_valid("ghn,ei") == False
    assert is_valid("leamdf") == True
