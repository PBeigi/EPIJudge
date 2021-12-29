from test_framework import generic_test
import collections

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_counter = collections.Counter(letter_text)
    for c in magazine_text:
        if c in letter_counter:
            letter_counter[c]-=1
            if letter_counter[c]==0:
                letter_counter.pop(c)
    return len(letter_counter.keys()) == 0





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
