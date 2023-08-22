from roman_to_int import roman_to_int


def test_roman_to_int():
    assert (roman_to_int("IV") == 4)
    assert (roman_to_int("IVD") == 504)
    assert (roman_to_int("VI") == 6)
    assert (roman_to_int("IX") == 9)
    assert (roman_to_int("XI") == 11)
    assert (roman_to_int("XL") == 40)
    assert (roman_to_int("LX") == 60)
    assert (roman_to_int("XC") == 90)
    assert (roman_to_int("CX") == 110)
    assert (roman_to_int("CD") == 400)
    assert (roman_to_int("DC") == 600)
    assert (roman_to_int("CM") == 900)
    assert (roman_to_int("MC") == 1100)
    assert (roman_to_int("LVIII") == 58)
    assert (roman_to_int("III") == 3)
    assert (roman_to_int("MCMX") == 1910)
    assert (roman_to_int("MCMXCIV") == 1994)
