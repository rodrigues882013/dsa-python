from typing import List, Tuple, Optional


class Graph:
    def __init__(self, node_number: int, edge_list: List[Tuple[int, int, Optional[int]]]):
        self.__storage = self.__build_graph_by_matrix(node_number, edge_list)

    @staticmethod
    def __build_graph_by_matrix(node_number, edge_list: List[Tuple[int, int, Optional[int]]]) -> List[List[int]]:
        max_item = sorted(edge_list, key=lambda x: x[1], reverse=True)[0][1]

        node_number = max_item + 1 if node_number < max_item else max_item

        m = [[0 for _ in range(node_number)] for _ in range(node_number)]

        for idx in range(len(edge_list)):
            node_one, node_two, weight = edge_list[idx]

            if weight:
                m[node_one][node_two] = weight

            else:
                m[node_one][node_two] += 1

        return m

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

    def get_topological_ordering(self):
        pass

    def find_shortest_path(self, start):
        pass


if __name__ == '__main__':
    g = Graph(6, [
        (0, 1, 3),
        (0, 2, 2),
        (0, 5, 3),
        (1, 3, 1),
        (1, 2, 6),
        (2, 3, 1),
        (2, 4, 10),
        (3, 4, 5),
        (5, 4, 7)
    ])

    print(g.dijkstra(0))
