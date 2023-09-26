from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50.0
    assert convert("3/4") == 75.0
    assert convert("2/3") == 66.67
    assert convert("0/1") == 0.0
    assert convert("1/0") == None
    assert convert("a/b") == None


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == 50
    assert gauge(99) == "F"
    assert gauge(100) == "F"
