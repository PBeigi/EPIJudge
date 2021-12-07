from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    st = []
    m = {
        '}':'{',
        ')':'(',
        ']': '['
    }
    for c in s:
        if c in m:
            if not len(st):
                return False
            most_recent = st.pop()
            if m[c] != most_recent:
                return False
        else:
            st.append(c)
    if len(st) !=0:
        return False
    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
