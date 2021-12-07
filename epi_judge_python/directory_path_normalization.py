from test_framework import generic_test



def shortest_equivalent_path(path: str) -> str:
    st = []
    if path[0] == '/':
        st.append('/')
    for token in (token for token in path.split('/') if token not in ['.', '']):
        if token == '..':
            if not st:
                st.append(token)
            elif st[-1] == '..':
                st.append(token)
            elif st[-1] == '/':
                raise Exception()
            else:
                st.pop()
        else:
            st.append(token)
    res =  '/'.join(st)
    return res[res.startswith('//'):]






if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
