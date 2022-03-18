from abc import ABC, abstractmethod
from enum import Enum


class Method(Enum):
    DIJKSTRA = 1
    BRUTE_FORCE = 2
    BELLMAN_FORD = 3


class Edge:
    def __init__(self, to: int, cost: float):
        self._to = to
        self._cost = cost


class Graph(ABC):

    @abstractmethod
    def bfs(self, start: int) -> list[int]:
        pass

    @abstractmethod
    def dfs(self, start: int, visited: set) -> list[int]:
        pass

    @abstractmethod
    def sort_topologically(self) -> list[int]:
        pass

    @abstractmethod
    def find_shortest_path(self, start: int, by_method: Method) -> list[int]:
        pass
