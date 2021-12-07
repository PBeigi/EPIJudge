from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALE_FACTOR = 2
    def __init__(self, capacity: int) -> None:
        self.entries = [0] * capacity
        self.head = self.tail = self.entry_count = 0

    def enqueue(self, x: int) -> None:
        if self.entry_count == len(self.entries): # resize
            self.entries = self.entries[self.head:] + self.entries[:self.head] + [0]*(self.self.entry_count*self.SCALE_FACTOR - self.entry_count)
            self.head = 0
            self.tail = self.entry_count
        self.entries[self.tail] = x


    def dequeue(self) -> int:
        # TODO - you fill in here.
        return 0

    def size(self) -> int:
        # TODO - you fill in here.
        return 0


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
