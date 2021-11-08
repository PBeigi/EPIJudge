from test_framework import generic_test


def look_and_say(n: int) -> str:
    def next_number(s):
        i = 0
        res = []
        while i < len(s):
            j = i
            count = 0
            while j < len(s) and s[j] == s[i]:
                j+=1
                count+=1
            res.append(str(count))
            res.append(s[i])
            i = j
        return ''.join(res)

    s = '1'
    for _ in range(n-1):
        s = next_number(s)
    return s

    previous = '1'
    for _ in range(n-1):
        i = 0
        res = []
        while i < len(previous):
            count = 0
            j = i
            while j < len(previous) and previous[j] == previous[i]:
                count+=1
                j+=1
            res.append(str(count))
            res.append(str(previous[i]))
            i = j
        previous = ''.join(res)
    return previous





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
