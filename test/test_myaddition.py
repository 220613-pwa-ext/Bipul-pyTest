from uitility.my_addition import my_addition, my_subtraction


def test_1():
    assert my_addition(20, 30) == 50


def test_2():
    assert my_addition(2.5,  3) == 5.5


def test_3():
    assert my_subtraction(10, 5) == 5

