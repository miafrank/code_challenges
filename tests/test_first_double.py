from challenges.first_double import first_double


def test_first_double():
    test_one = [2, 1, 3, 5, 3, 2]
    test_two = [2, 2]
    test_three = [2, 4, 3, 5, 1]

    expected_one = 3
    expected_two = 2
    expected_three = -1

    assert (first_double(test_one)) == expected_one
    assert (first_double(test_two)) == expected_two
    assert (first_double(test_three)) == expected_three
