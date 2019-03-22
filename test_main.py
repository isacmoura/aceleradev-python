import main as m


def test_1():
    assert isinstance(m.q_1(), int)

def test_2():
    assert isinstance(m.q_2(), int)

def test_3():
    r = m.q_3()
    assert (
        isinstance(r, list) and
        all(isinstance(y, str) for y in r)
    )

def test_4():
    r = m.q_4()
    assert (
        isinstance(r, list) and
        all(isinstance(y, str) for y in r)
    )

def test_5():
    r = m.q_5()
    assert (
        isinstance(r, list) and
        all(isinstance(y, str) for y in r)
    )

def test_6():
    r = m.q_6()
    assert (
        isinstance(r, dict) and
        all(isinstance(y, int) for y in r.keys()) and
        all(isinstance(y, int) for y in r.values())
    )
