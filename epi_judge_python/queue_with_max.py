import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueWithMax:
    def __init__(self):
        self.q = collections.deque()
        self.max_q = collections.deque()
    def enqueue(self, x: int) -> None:
        if self.max_q:
            if self.max_q[-1] < x:
                while self.max_q and self.max_q[-1] < x:
                    self.max_q.pop()
                self.max_q.append(x)
            else:
                self.max_q.append(x)
        else:
            self.max_q.append(x)
        self.q.append(x)




    def dequeue(self) -> int:
        res = self.q.popleft()
        if self.max_q and self.max_q[0] == res:
            self.max_q.popleft()
        return res

    def max(self) -> int:
        return self.max_q[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
