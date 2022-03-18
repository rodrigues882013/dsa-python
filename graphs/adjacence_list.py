import math
from typing import List, Tuple, Optional, Dict

from graphs.common import Graph, Method
from linears.queues import PriorityQueue
from collections import deque


class AGraph(Graph):
    def __init__(self, node_number: int, edge_list: List[Tuple[int, int, Optional[int]]]):
        self.__storage = self.__build_graph_by_list(node_number, edge_list)

    @staticmethod
    def __build_graph_by_list(node_number: int, edge_list: List[Tuple[int, int, Optional[int]]]) -> Dict[
        int, List[Tuple[int, Optional[int]]]]:
        storage = {}

        for i in range(node_number):
            storage[i] = []

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

        def helper(_start: int):
            path.append(_start)

            visited.add((_start, None))

            for v in self.__storage[_start]:
                if (v[0], None) not in visited:
                    helper(v[0])

        helper(start)

        return path

    def __dijkstra_with_target_node(self, start: int, end: int) -> Optional[float]:
        number_of_vertices = len(self.__storage)
        visited = [False] * number_of_vertices
        distances = [math.inf] * number_of_vertices
        distances[0] = 0
        pq = PriorityQueue((0, start))  # (distance, edge)

        while not pq.is_empty():
            minimum_value, node_id = pq.dequeue()
            visited[node_id] = True

            if minimum_value > distances[node_id]:
                continue

            for edge in self.__storage[node_id]:

                if visited[edge[0]]:
                    continue

                new_distance = distances[node_id] + edge[1]

                if new_distance < distances[edge[0]]:
                    distances[edge[0]] = new_distance
                    pq.enqueue((new_distance, edge[0]))

            if end and node_id == end:
                return distances[end]

        return None

    def __dijkstra_without_target(self, start) -> List[float]:
        number_of_vertices = len(self.__storage)
        visited = [False] * number_of_vertices
        distances = [math.inf] * number_of_vertices
        distances[start] = 0
        pq = PriorityQueue((0, start))  # (distance, edge)

        while not pq.is_empty():
            minimum_value, node_id = pq.dequeue()
            visited[node_id] = True

            if minimum_value > distances[node_id]:
                continue

            for edge in self.__storage[node_id]:

                if visited[edge[0]]:
                    continue

                new_distance = distances[node_id] + edge[1]

                if new_distance < distances[edge[0]]:
                    distances[edge[0]] = new_distance
                    pq.enqueue((new_distance, edge[0]))

        return distances

    def __bellman_ford_without_target(self, start) -> List[float]:
        number_of_vertices = len(self.__storage)
        distances = [math.inf] * number_of_vertices
        distances[start] = 0

        for _ in range(number_of_vertices - 1):
            for vertex in range(0, number_of_vertices):
                for edge in self.__storage[vertex]:
                    new_distance = distances[vertex] + edge[1]

                    if new_distance < distances[edge[0]]:
                        distances[edge[0]] = new_distance

        # Running a second time, at this point any value from distance should be change,
        # if so there is a cycle in the graph
        for _ in range(number_of_vertices - 1):
            for vertex in range(0, number_of_vertices):
                for edge in self.__storage[vertex]:
                    if distances[vertex] + edge[1] < distances[edge[0]]:
                        distances[edge[0]] = -math.inf

        return distances


    def sort_topologically(self):
        number_of_vertices = len(self.__storage)
        visited = [False] * number_of_vertices
        ordering_queue = deque([])

        # It is just a dfs with some tricks
        def helper(start: int):
            visited[start] = True

            for vs in self.__storage[start]:
                if not visited[vs[0]]:
                    helper(vs[0])

            ordering_queue.appendleft((start, None))

        for at in range(number_of_vertices):
            if at in self.__storage and not visited[at]:
                helper(at)

        return list(ordering_queue)

    def __find_shortest_path_by_dijkstra(self, start, end):
        pass

    def __find_shortest_path_by_brute_force(self, start, end):
        # To determine the single shortest path we need that all vertices have a topological order
        nodes_in_topological_order = self.sort_topologically()

        # Every initial distance is infinite
        distances = [math.inf] * len(self.__storage)

        # We're departing from vertex start, obviously the distance for itself is zero
        distances[start] = 0

        # From each vertex we'll calculate the distances following the topological order array
        for node in self.__storage.keys():
            node_tuple = nodes_in_topological_order[node]
            node_idx = node_tuple[0]  # Node -> (Node, Weight)

            if distances[node_idx] != math.inf:

                edges_from_node = self.__storage.get(node_idx)

                # We'll calculate from the node node_idx following the all its out-degree edges
                for edge in edges_from_node:
                    new_distance = distances[node_idx] + edge[1]
                    distances[edge[0]] = min(distances[edge[0]], new_distance)

        return distances

    def find_shortest_path(self, start, by_method: Method = None):

        if by_method == Method.DIJKSTRA:
            ans = self.__dijkstra_without_target(0)
        elif by_method == Method.BELLMAN_FORD:
            ans = self.__bellman_ford_without_target(start)
        else:
            ans = self.__find_shortest_path_by_brute_force(start, 0)

        return ans


if __name__ == '__main__':

    # Use that input to test Bellman-Ford
    g = AGraph(9, [
        (0, 1, 1),
        (1, 2, 1),
        (2, 4, 1),
        (4, 3, -3),
        (3, 2, 1),
        (1, 5, 4),
        (1, 6, 4),
        (5, 6, 5),
        (6, 7, 4),
        (5, 7, 3)
    ])

    """
    0 - 1
    
    """
    # [(0, None), (5, None), (1, None), (2, None), (3, None), (4, None)] <- right
    print(g.find_shortest_path(0, Method.BELLMAN_FORD))

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
