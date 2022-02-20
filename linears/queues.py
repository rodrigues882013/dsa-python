import abc
from heapq import heapify, heappop, heappush
from typing import TypeVar, List, Optional

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
