from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    valid = set()
    for num in range(n+1):
        i = num
        if i not in valid:
            while i!=1 and i not in valid:
                i = 3*i+1 if i%2==1 else i/2
                valid.add(i)
            if i == 1:
                valid.add(num)
    return n in valid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
