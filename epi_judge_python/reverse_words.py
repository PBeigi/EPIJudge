import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    i = 0
    j = len(s) - 1
    def reverse_s(s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
    reverse_s(s, i, j)
    i = 0
    while i < len(s):
        if s[i] != ' ':
            word_end = i
            while word_end < len(s) and s[word_end]!=' ':
                word_end+=1
            j = word_end-1
            reverse_s(s, i, j)
            i = word_end
        elif s[i] == ' ':
            i+=1

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
