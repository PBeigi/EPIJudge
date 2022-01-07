import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import heapq
# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # h = []
    # A.sort(key=lambda a:a.start)
    # for start, finish in A:
    #     if h and h[0] < start:
    #         heapq.heapreplace(h, finish)
    #     else:
    #         heapq.heappush(h, finish)
    #
    # return len(h)

    # A.sort(key=lambda x:x.start)
    # heap = []  # stores the end time of intervals
    # for i in A:
    #     if heap and i.start >= heap[0]:
    #         # means two intervals can use the same room
    #         heapq.heapreplace(heap, i.finish)
    #     else:
    #         # a new room is allocated
    #         heapq.heappush(heap, i.finish)
    # return len(heap)
    times = []
    EndPoint = collections.namedtuple('EndPoint', ('time', 'is_start'))
    times = [p for a in A for p in (EndPoint(time=a.start, is_start=True), EndPoint(time=a.finish, is_start=False))]
    count = 0
    max_count = float('-inf')
    times.sort(key=lambda e: (e.time, not e.is_start))
    for e in times:
        if e.is_start:
            count+=1
        else:
            count-=1
        max_count = max(max_count, count)
    return max_count



@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
