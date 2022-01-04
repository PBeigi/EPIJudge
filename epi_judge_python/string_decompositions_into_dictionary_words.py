from typing import List

from test_framework import generic_test
import collections
import copy
def find_all_substrings(s: str, words: List[str]) -> List[int]:
    word_size = len(words[0])
    concat_size = word_size * len(words)
    res = []
    def find_substrings(start):
        left = start
        right = start
        c = collections.Counter(words)
        missing = len(c)
        while right <= len(s) - word_size:
            word = s[right:right+word_size]
            if word in c:
                c[word]-=1
                if c[word]==0:
                    missing-=1
            while missing == 0:
                if (right - left + word_size) == concat_size:
                    res.append(left)
                word = s[left:left+word_size]
                if word in c:
                    c[word]+=1
                    if c[word]==1:
                        missing+=1
                left+=word_size
            right+=word_size
    for start in range(len(words[0])):
        find_substrings(start)
    return res




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
