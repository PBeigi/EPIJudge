from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    i = 0
    j = 0
    res = []
    while i < len(s):
        while j < len(s) and s[j].isdigit():
            j+=1
        res += int(s[i:j]) * s[j]
        i = j + 1
        j = i
    return ''.join(res)




def encoding(s: str) -> str:
    i = 0
    j = 0
    res = []
    while i < len(s):
        count = 0
        while j < len(s) and s[j] == s[i]:
            count+=1
            j+=1
        res.append(f"{count}{s[i]}")
        i = j
    return ''.join(res)



def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
