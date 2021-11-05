from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if num_as_string == '0':
        return num_as_string
    res = 0
    sign = 1
    if num_as_string[0] in '-+':
        sign = -1 if num_as_string[0] == '-' else 1
        num_as_string = num_as_string[1:]
    m = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    for c in num_as_string:
        if c in m:
            d = m[c]
        else:
            d = int(c)
        res = res * b1 + d
    ans = []
    while res:
        rem = res % b2
        if rem >=10:
            v = chr(rem + 55)
        else:
            v = str(rem)
        ans.append(v)
        res = res // b2
    if sign == -1:
        ans.append('-')
    return ''.join(reversed(ans))





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
