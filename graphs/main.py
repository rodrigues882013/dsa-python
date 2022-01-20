from enum import Enum
from functools import reduce
from itertools import chain
from typing import List, Tuple, Optional, Dict
import math


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
    def __build_graph_by_list(edge_list: List[Tuple[int, int, Optional[int]]]) -> Dict[int, List[Tuple[int, Optional[int]]]]:
        storage = {}
        edges = [(e[0], e[1]) for e in edge_list]
        nodes = set()

        for i in edges:
            nodes.add(i[0])
            nodes.add(i[1])

        for node in nodes:
            if node not in storage:
                storage[node] = []

        for edge in edge_list:
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
                    if (v[0], None) not in visited:
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

    def dfs_topological_sort_helper(self, idx, ordering, start: int, v) -> int:

        if self.__storage_type == StorageType.ADJACENCY_MATRIX:
            pass
        else:
            v[start] = True

            for vs in self.__storage[start]:
                if not v[vs[0]]:
                    idx = self.dfs_topological_sort_helper(idx, ordering, vs[0], v)

        ordering[idx] = (start, None)
        return idx - 1

    def get_topological_ordering(self):
        n = len(self.__storage)
        v = [False] * n
        ordering = [0] * n
        idx = n - 1

        for at in range(n):
            if at in self.__storage and not v[at]:
                idx = self.dfs_topological_sort_helper(idx, ordering, at, v)

                # for node_id in visited_nodes:
                #     ordering[idx] = node_id[0]
                #     v[node_id[0]] = True
                #     idx -= 1

        return ordering

    def find_shortest_path(self, start):

        # To determine the single shortest path we need that all vertices have a topological order
        nodes_in_topological_order = self.get_topological_ordering()

        # Every initial distance is infinite
        distances = [math.inf] * len(self.__storage)

        # We're departing from vertex start, obviously the distance for itself is zero
        distances[start] = 0

        # From each vertex we'll calculate the distances following the topological order array
        for node in self.__storage.keys():
            node_tuple = nodes_in_topological_order[node]
            node_idx = node_tuple[0] # Node -> (Node, Weight)

            if distances[node_idx] != math.inf:

                edges_from_node = self.__storage.get(node_idx)

                # We'll calculate from the node node_idx following the all its out-degree edges
                for edge in edges_from_node:
                    new_distance = distances[node_idx] + edge[1]
                    distances[edge[0]] = min(distances[edge[0]], new_distance)

        return distances


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
    ], storage_type=StorageType.ADJACENCY_LIST)

    """
    0 - 1
    
    """

    print(g.find_shortest_path(0)[6])

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
