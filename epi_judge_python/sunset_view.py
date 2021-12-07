import collections
from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    BuildingHeightWithID = collections.namedtuple('B',('height', 'id'))
    st = [] # candidate buildings potential of having sunset
    for i,height in enumerate(sequence):
        while len(st) and st[-1].height <= height:
            st.pop()
        st.append(BuildingHeightWithID(height,i))
    res = [building.id for building in reversed(st)]
    return res










def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
