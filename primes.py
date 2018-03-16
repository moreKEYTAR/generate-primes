"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""
    primes = []

    if count >= 1:
        primes.append(2)

    num_tries = 0
    while len(primes) < count:
        previous_try = primes[-1] + num_tries
        current_try = previous_try + 1


        if current_try % 2 == 0:  # if it is even, it is not prime, and we need
                                    # to start the while loop again with a higher number
            num_tries += 1        # makes helps us change the current_try to one more
        else:
            x = 1
            while (current_try - x) >= 2:

                if current_try - x == 2:  # if we have gotten here, then it is prime
                    primes.append(current_try)
                    num_tries = 0
                    break
                else:
                    if current_try % (current_try - x) == 0:  # it has a factor, so we need to try another number and start again
                        num_tries += 1
                        x = 1
                        break
                    else:
                        x += 1

    return primes


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
