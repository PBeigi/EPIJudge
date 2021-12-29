from test_framework import generic_test
import collections

def can_form_palindrome(s: str) -> bool:
    m = collections.defaultdict(int)
    odd_count = 0
    for c in s:
        if m[c] % 2 == 1:
            odd_count -=1
        else:
            odd_count +=1
        m[c]+=1
    if odd_count <=1:
        return True
    return False




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
