import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import heapq
Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age(people: List[Person]) -> None:
    # m = collections.defaultdict(int)
    # for person in people:
    #     m[person.age]+=1
    m = collections.Counter((person.age for person in people))
    age_index = collections.defaultdict(int)
    cum_count = 0
    for age, count in m.items():
        age_index[age] = cum_count
        cum_count+=count
    while age_index:
        from_age = next(iter(age_index))
        from_age_index = age_index[from_age]
        to_age = people[from_age_index].age
        to_age_index = age_index[to_age]
        people[from_age_index], people[to_age_index] = people[to_age_index], people[from_age_index]
        m[to_age]-=1
        if m[to_age] == 0:
            del age_index[to_age]
        else:
            age_index[to_age] = to_age_index + 1










@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('group_equal_entries.py',
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
