from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LruCache:
    def __init__(self, capacity: int) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = dict()
        self.capacity = capacity

    def lookup(self, isbn: int) -> int:
        if isbn not in self.m:
            return -1
        n = self.m[isbn]
        self.remove(n)
        self.add(n)
        return n.value


    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.m:
            n = self.m[isbn]
            self.remove(n)
            self.add(n)
        else:
            if self.capacity == len(self.m):
                n = self.head.next
                self.remove(n)
                self.m.pop(n.key)
            n = Node(key=isbn, value=price)
            self.add(n)
            self.m[isbn] = n

    def erase(self, isbn: int) -> bool:
        if isbn not in self.m:
            return False
        n = self.m[isbn]
        self.remove(n)
        self.m.pop(isbn)
        return True

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
