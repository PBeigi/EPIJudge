from test_framework import generic_test


def snake_string(s: str) -> str:
    first = []
    second = []
    third = []
    for i,c in enumerate(s):
        if i%2==0:
            second.append(c)
        elif i%4==1:
            first.append(c)
        elif i%2==1:
            third.append(c)
    res = first + second + third
    return ''.join(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
