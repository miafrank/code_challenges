from challenges.happy_number import happy_number


def test_majority_element():
    assert happy_number(2) is False
    assert happy_number(19) is True
