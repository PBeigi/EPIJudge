from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    results = []
    def is_valid(s):
        return len(s)==1 or (s[0]!='0' and int(s) <= 255)

    for i in range(1, min(4, len(s))):
        part_1 = s[:i]
        if is_valid(part_1):
            for j in range(i+1, min(i+4, len(s))):
                part_2 = s[i:j]
                if is_valid(part_2):
                    for k in range(j+1, min(j+4, len(s))):
                        part_3 = s[j:k]
                        part_4 = s[k:]
                        if is_valid(part_3) and is_valid(part_4):
                            results.append(f"{part_1}.{part_2}.{part_3}.{part_4}")
    return results



def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
