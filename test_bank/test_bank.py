from bank import value
import pytest


def test_type():
    with pytest.raises(AttributeError):
        value(2)


def test_index():
    with pytest.raises(IndexError):
        value("")


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_h_not_hello():
    assert value("hello there") == 0


def test_h():
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("How is going") == 20


def test_100():
    assert value("What\’s up") == 100


def test_hello_final():
    assert value("and hello") == 100 or value("AND HELLO") == 100
