import math
from typing import List, Tuple, Optional, Dict

from linears.queues import PriorityQueue
from collections import deque


class Graph:
    def __init__(self, node_number: int, edge_list: List[Tuple[int, int, Optional[int]]]):
        self.__storage = Graph.__build_graph_by_list(edge_list)

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

            visited.add((_start, None))

            for v in self.__storage[_start]:
                if (v[0], None) not in visited:
                    inner_dfs(v[0])

        inner_dfs(start)

        return path

    def dijkstra(self, start):
        number_of_nodes = len(self.__storage)
        visited = [False] * number_of_nodes
        distances = [math.inf] * number_of_nodes
        distances[0] = 0
        queue = PriorityQueue((0, start))

        while not queue.is_empty():
            minimum_value, idx = queue.dequeue()
            visited[idx] = True

            for edge in self.__storage[idx]:
                if not visited[edge[0]]:
                    new_distance = distances[idx] + edge[1]
                    if new_distance < distances[edge[0]]:
                        distances[edge[0]] = new_distance
                        queue.enqueue((new_distance, edge[0]))

        return distances

    def find_shortest_path_by_dijkstra(self, start, end):
        pass

    def dfs_topological_sort_helper(self, ordering, start: int, v):

        v[start] = True

        for vs in self.__storage[start]:
            if not v[vs[0]]:
                self.dfs_topological_sort_helper(ordering, vs[0], v)

        #ordering[idx] = (start, None)
        ordering.appendleft((start, None))
        #return idx - 1

    def get_topological_ordering(self):
        number_of_nodes = len(self.__storage)
        visited = [False] * number_of_nodes
        ordering = [0] * number_of_nodes
        ordering_queue = deque([])
        #idx = number_of_nodes - 1

        for at in range(number_of_nodes):
            if at in self.__storage and not visited[at]:
                self.dfs_topological_sort_helper(ordering_queue, at, visited)
        return ordering_queue

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
    ])

    """
    0 - 1
    
    """
    # [(0, None), (5, None), (1, None), (2, None), (3, None), (4, None)] <- right
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
