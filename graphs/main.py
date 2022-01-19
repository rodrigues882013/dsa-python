from enum import Enum
from typing import List, Tuple, Optional, Dict


class StorageType(Enum):
    ADJACENCY_LIST = 1
    ADJACENCY_MATRIX = 2


class Graph:
    def __init__(self, node_number: int, edge_list: List[Tuple[int, int, Optional[int]]],
                 storage_type: StorageType = StorageType.ADJACENCY_MATRIX):

        self.__storage = self.__build(node_number, edge_list, storage_type)
        self.__storage_type = storage_type

    def __build(self, node_number: int, edge_list: List[Tuple[int, int, Optional[int]]], storage_type: StorageType):

        if storage_type == StorageType.ADJACENCY_MATRIX:
            return self.__build_graph_by_matrix(node_number, edge_list)
        else:
            return self.__build_graph_by_list(edge_list)

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

    @staticmethod
    def __build_graph_by_list(edge_list: List[Tuple[int, int, Optional[int]]]) -> Dict[
        int, List[Tuple[int, Optional[int]]]]:
        storage = {}

        for edge in edge_list:
            if edge[0] not in storage:
                storage[edge[0]] = []
            storage[edge[0]].append((edge[1], edge[2]))

        return storage

    def bfs(self, start) -> List[int]:
        queue = [start]
        visited = set()
        visited.add(start)
        path = []

        while len(queue) > 0:

            popped = queue.pop(0)
            path.append(popped)

            if self.__storage_type == StorageType.ADJACENCY_MATRIX:

                for idx in range(len(self.__storage)):
                    if self.__storage[popped][idx] > 0 and idx not in visited:
                        visited.add(idx)
                        queue.append(idx)

            else:
                for v in self.__storage[start]:
                    if v[0] not in visited:
                        visited.add(v[0])
                        queue.append(v[0])
                        # self.dfs(v[0], visited)
        return path

    def dfs(self, start: int, visited: set) -> List[int]:
        path = []

        def inner_dfs(_start: int):
            path.append(_start)

            if self.__storage_type == StorageType.ADJACENCY_MATRIX:
                visited.add(_start)

                for idx in range(len(self.__storage)):
                    if self.__storage[_start][idx] > 0 and idx not in visited:
                        inner_dfs(idx)
            else:
                visited.add((_start, None))

                for v in self.__storage[_start]:
                    if v not in visited:
                        inner_dfs(v[0])

        inner_dfs(start)

        return path

        # print(start)
        #
        # if self.__storage_type == StorageType.ADJACENCY_MATRIX:
        #     visited.add(start)
        #
        #     for idx in range(len(self.__storage)):
        #         if self.__storage[start][idx] > 0 and idx not in visited:
        #             self.dfs(idx, visited)
        # else:
        #     visited.add((start, None))
        #
        #     for v in self.__storage[start]:
        #         if v not in visited:
        #             self.dfs(v[0], visited)

    def dijkstra(self, start, end):
        pass

    def get_topological_ordering(self):
        n = len(self.__storage)
        v = [False] * n
        ordering = [0] * n
        idx = n - 1

        for at in range(n):
            if not v[at]:
                visited_nodes = set()
                self.dfs(at, visited_nodes)

                for node_id in visited_nodes:
                    ordering[idx] = node_id[0]
                    v[node_id[0]] = True
                    idx -= 1

        return ordering


if __name__ == '__main__':
    g = Graph(6, [
        (0, 1, None),
        (0, 2, None),
        (1, 2, None),
        (2, 0, None),
        (2, 3, None),
        (3, 2, None),
        (3, 1, None),
        (1, 3, None),
        (3, 3, None),
        (30, 90, None),
        (90, 30, None)
    ], storage_type=StorageType.ADJACENCY_LIST)

    """
    0 - 1
    
    """

    print(g.get_topological_ordering())

    """
    storage = {}
        path = []
        
        def build_graph():
            
            for edge in edges:
                if edge[0] not in storage:
                    storage[edge[0]] = []
                storage[edge[0]].append(edge[1])
                
                if edge[1] not in storage:
                    storage[edge[1]] = []
                storage[edge[1]].append(edge[0])
        
        
        def dfs(_start: int, visited: set):
            path.append(_start)
            visited.add(_start)

            if _start in storage:
                for v in storage[_start]:
                    if v not in visited:
                        dfs(v, visited)
           
        
        
        build_graph()
        dfs(start, set())
    """
