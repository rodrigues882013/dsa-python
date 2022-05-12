from typing import Optional


class CircularQueueError(Exception):
    pass


"""
A wrapper class for the list components
"""


class ListNode:
    def __init__(self, value=Optional[int], next_pt: Optional['ListNode'] = None, prev_pt: Optional['ListNode'] = None):
        self.value = value
        self.next = next_pt
        self.prev = prev_pt


"""
A simple circular queue data structure that allows O(1) operations using O(n) spaces
"""


class CircularQueue:

    def __init__(self, k: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.maximum_size = k
        self.current_size = 0
        self.__set_up()

    def __set_up(self):
        self.head.next = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head

    def enqueue(self, value: int) -> bool:

        if self.is_full():
            raise CircularQueueError("Queue is full, dequeue something to add more values")

        new_node = ListNode(value)

        if self.head.next is None:
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = self.tail
            self.tail.prev = new_node

        else:
            new_node.next = self.tail
            self.tail.prev.next = new_node
            new_node.prev = self.tail.prev
            self.tail.prev = new_node

        self.current_size += 1
        return True

    def dequeue(self) -> int:
        if self.is_empty():
            raise CircularQueueError("Queue is empty")

        dequeued = self.head.next.value
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.current_size -= 1
        return dequeued

    def head(self) -> int:
        if self.tail.prev != self.head:
            return self.head.next.value

        return -1

    def tail(self) -> int:
        if self.tail.prev != self.head:
            return self.tail.prev.value

        return -1

    def is_empty(self) -> bool:
        return self.current_size == 0

    def is_full(self) -> bool:
        return self.current_size == self.maximum_size
