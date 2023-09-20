from twttr import shorten
import pytest


def test_a():
    assert shorten("fala") == "fl" or shorten("fAlA") == "fl"


def test_upperA():
    assert shorten("FALA") == "FL" or shorten("FaLa") == "FL"


def test_e():
    assert shorten("lEr") == "lr" or shorten("ler") == "lr"


def test_upperE():
    assert shorten("LER") == "LR" or shorten("LER") == "LR"


def test_i():
    assert shorten("IrIs") == "rs" or shorten("iris") == "rs"


def test_upperI():
    assert shorten("IRIS") == "RS" or shorten("iRiS") == "RS"


def test_o():
    assert shorten("OvO") == "v" or shorten("ovo") == "v"

def test_upperO():
    assert shorten("OVO") == "V" or shorten("oVo") == "V"


def test_u():
    assert shorten("UrUbU") == "rb" or shorten("urubu") == "rb"

def test_upperU():
    assert shorten("URUBU") == "RB" or shorten("uRuBu") == "RB"
