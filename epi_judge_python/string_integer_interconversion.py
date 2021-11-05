from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'
    res = []
    sign = 1 if x >= 0 else -1
    x = abs(x)
    while x:
        rem = x % 10
        res.append(chr(rem + ord('0')))
        x = x // 10
    if sign == -1:
        res.append('-')
    s = ''.join(reversed(res))
    return s



def string_to_int(s: str) -> int:
    res = 0
    if s[0].isdigit():
        sign = 1
    else:
        sign = 1 if s[0]=='+' else -1
        s = s[1:]
    for c in s:
        d = ord(c) - ord('0')
        res = res * 10 + d
    return res*sign





def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
