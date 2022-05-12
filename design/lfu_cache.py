class Node:
    def __init__(self, key=0, value=0, frequency=1):
        self.key = key
        self.value = value
        self.frequency = frequency
        self.next = None
        self.prev = None


class DoubledLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.__size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node
        self.__size += 1

    def remove(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

        self.__size -= 1

    def pop_tail(self):
        popped = self.tail.prev
        self.remove(popped)
        #self.__size -= 1
        return popped

    def move_to_head(self, node):
        self.remove(node)
        self.add(node)

    def size(self):
        return self.__size


class LFUCache:

    def __init__(self, capacity: int):
        self.frequencies = {}
        self.nodes = {}
        self.max_len = capacity
        self.len = 0
        self.min_frequency = 0

    def move_between_buckets(self, node):
        freq = node.frequency
        self.frequencies[freq].remove(node)

        if self.min_frequency == freq and self.frequencies[freq].size() == 0:
            self.min_frequency += 1

        node.frequency += 1
        if node.frequency not in self.frequencies:
            self.frequencies[node.frequency] = DoubledLinkedList()
        self.frequencies[node.frequency].add(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.move_between_buckets(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.move_between_buckets(node)

        else:

            if self.len == self.max_len:
                node = self.frequencies[self.min_frequency].pop_tail()
                del self.nodes[node.key]
                self.len -= 1

            new_node = Node(key, value)
            self.nodes[key] = new_node

            if 1 not in self.frequencies:
                self.frequencies[1] = DoubledLinkedList()

            self.frequencies[1].add(new_node)
            self.min_frequency = 1
            self.len += 1


def main():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.get(3)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)


if __name__ == '__main__':
    main()
