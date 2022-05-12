import abc
from heapq import heapify, heappop, heappush
from typing import TypeVar, List, Optional

from commons import ListNode

T = TypeVar("T")


class Operation:

    @abc.abstractmethod
    def enqueue(self, data) -> None:
        pass

    @abc.abstractmethod
    def dequeue(self) -> T:
        pass

    @abc.abstractmethod
    def is_empty(self) -> bool:
        pass


class PriorityQueue(Operation):

    def __init__(self, data=Optional[T]):
        self.__storage: List[T] = []
        heapify(self.__storage)

        if data:
            self.enqueue(data)

    def enqueue(self, data: T) -> None:
        heappush(self.__storage, data)

    def dequeue(self) -> T:
        return heappop(self.__storage)

    def is_empty(self) -> bool:
        return len(self.__storage) == 0


class CircularQueue:

    def __init__(self, k: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head
        self.maximum_size = k
        self.current_size = 0

    def enQueue(self, value: int) -> bool:

        if self.current_size >= self.maximum_size:
            return False

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

    def deQueue(self) -> bool:
        if self.tail.prev == self.head and self.current_size == 0:
            return False

        dequeued = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.current_size -= 1
        return True

    def Front(self) -> int:
        if self.tail.prev != self.head:
            return self.head.next.value

        return -1

    def Rear(self) -> int:
        if self.tail.prev != self.head:
            return self.tail.prev.value

        return -1

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.maximum_size


def main():
    q = CircularQueue(5)
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.enQueue(4)
    q.enQueue(5)
    #
    # print(q.Rear())
    # print(q.Front())

    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    print(q.Front())

    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.enQueue(4)
    q.enQueue(5)
    print(q.Front())
    print(q.Rear())





if __name__ == '__main__':
    main()
