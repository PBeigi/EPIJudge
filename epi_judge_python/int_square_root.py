from test_framework import generic_test


def square_root(k: int) -> int:
    left = 0
    right = k + 1

    while left < right:
        mid = left + (right - left) // 2
        if mid * mid > k:
            right = mid
        else:
            left = mid + 1
    return left - 1







if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
