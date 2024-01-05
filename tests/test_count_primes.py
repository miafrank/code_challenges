from challenges.count_primes import count_primes


def test_count_primes():
    assert count_primes(10) == 4
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    assert count_primes(2) == 0
