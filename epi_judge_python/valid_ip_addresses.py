from typing import List

from test_framework import generic_test

def dfs2(s, part_count, path, res):
    if part_count > 4:
        return
    if part_count==4 and len(s)==0:
        res.append(path[:-1])
    for i in range(1, min(4, len(s)+1)):
        part = s[:i]
        if len(part) == 1 or (part[0] != '0' and int(part) <= 255):
            dfs2(s[i:], part_count + 1, path + part + ".", res)

def dfs(s, cur_idx, part_count, path, res):
    if part_count > 4:
        return
    if part_count==4 and cur_idx >= len(s):
        res.append(path[:-1])
    for i in range(cur_idx+1,min(cur_idx+4, len(s)+1)):
        part = s[cur_idx:i]
        if len(part)==1 or (part[0]!='0' and int(part)<=255):
            #print(f"cur: {cur_idx}, part_count: {part_count}, section: {part}, path: {path}")
            dfs(s, i, part_count+1, path+part+".", res)


def get_valid_ip_address(s: str) -> List[str]:
    results = []
    dfs2(s,0,"", results)
    return results



def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
