from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self, x: int) -> None:
        if len(self.s2):
            while len(self.s2):
                self.s1.append(self.s2.pop())
        self.s1.append(x)

        while len(self.s1):
            self.s2.append(self.s1.pop())


    def dequeue(self) -> int:
        res = self.s2.pop()
        return res


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
