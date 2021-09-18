from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    is_prime = [False, False] + [True] * (n-1)
    primes = []
    for e in range(n+1):
        if is_prime[e]:
            primes.append(e)
            for v in range(e, n+1, e):
                is_prime[v] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
