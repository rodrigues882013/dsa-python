import math
from collections import deque
from typing import List, Tuple, Optional


class Graph:
    def __init__(self, grid: List[List[int]]):
        self.__storage = grid

    def bfs(self, start) -> List[int]:
        queue = [start]
        visited = set()
        visited.add(start)
        path = []

        while len(queue) > 0:

            popped = queue.pop(0)
            path.append(popped)

            for idx in range(len(self.__storage)):
                if self.__storage[popped][idx] > 0 and idx not in visited:
                    visited.add(idx)
                    queue.append(idx)

        return path

    def dfs(self, start: int, visited: set) -> List[int]:
        path = []

        def inner_dfs(_start: int):
            path.append(_start)

            visited.add(_start)

            for idx in range(len(self.__storage)):
                if self.__storage[_start][idx] > 0 and idx not in visited:
                    inner_dfs(idx)

        inner_dfs(start)
        return path

    def dijkstra(self, start):
        pass

    def find_shortest_path_by_dijkstra(self, start, end):
        pass

    def dfs_topological_sort_helper(self, idx, ordering, start: int, v) -> int:
        pass

    def sort_topologically(self):
        m = len(self.__storage)
        n = len(self.__storage[0])
        visited = set()
        ordering_queue = deque([])

        # It is just a dfs with some tricks
        def helper(row: int, col: int):
            visited.add((row, col))

            for (next_row, next_col) in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                if 0 <= next_row < m and 0 <= next_col < n and (next_row, next_col) not in visited and self.__storage:
                    helper(next_row, next_col)

            ordering_queue.appendleft((row, col))

        for i in range(m):
            return list(ordering_queue)


if __name__ == '__main__':
    # g = Graph(6, [
    #     (0, 1, 3),
    #     (0, 2, 2),
    #     (0, 5, 3),
    #     (1, 3, 1),
    #     (1, 2, 6),
    #     (2, 3, 1),
    #     (2, 4, 10),
    #     (3, 4, 5),
    #     (5, 4, 7)
    # ])

    g = Graph([
        [0, 3, 2, 0, 0, 3],
        [0, 0, 6, 1, 0, 0],
        [0, 0, 0, 1, 10, 0],
        [0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 7, 0]
    ])

    print(g.sort_topologically())
