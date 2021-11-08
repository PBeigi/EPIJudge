from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    i = 0
    sum = 0
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    while i < len(s):
        if i+1 < len(s) and m[s[i+1]] > m[s[i]]:
            # if ((s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')) or
            #     (s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C')) or
            #     (s[i]=='C' and (s[i+1]=='D' or s[i+1]== 'M'))):
                sum += m[s[i+1]] - m[s[i]]
                i+=2
        else:
            sum += m[s[i]]
            i += 1
    return sum




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
