from test_framework import generic_test
import functools

def rabin_karp(t: str, s: str) -> int:
    t_hash = 0
    s_hash = 0
    if len(t) < len(s):
        return -1
    for c in s:
        s_hash = s_hash * 26 + ord(c)
    for i in range(len(s)):
        t_hash = t_hash * 26 + ord(t[i])
    if t_hash == s_hash:
        return 0
    for i in range(len(s), len(t)):
        t_hash = t_hash - (26**(len(s)-1)) * ord(t[i - len(s)])
        t_hash = t_hash * 26 + ord(t[i])
        if s_hash == t_hash:
            return i - len(s) + 1
    return -1


def rabin_karp2(t: str, s: str) -> int:
    if len(s) > len(t):
        return -1
    t_hash = functools.reduce(lambda sum, c: sum * 26 + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda sum, c: sum * 26 + ord(c), s, 0)
    if t_hash == s_hash:
        return 0
    for i in range(len(s), len(t)):
        _hash = t_hash - (26 ** (len(s) - 1)) * ord(t[i - len(s)])
        t_hash = t_hash * 26 + ord(t[i])
        if s_hash == t_hash:
            return i - len(s) + 1
    return -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
