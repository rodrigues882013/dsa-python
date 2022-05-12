class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoubledLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def pop_tail(self):
        popped = self.tail.prev
        self.remove(popped)
        return popped

    def move_to_head(self, node):
        self.remove(node)
        self.add(node)


class LRUCache:

    def __init__(self, capacity: int):
        self.storage = {}
        self.capacity = capacity
        self.size = 0
        self.list = DoubledLinkedList()

    def get(self, key: int) -> int:
        if key in self.storage:
            retrived = self.storage[key]
            self.list.move_to_head(retrived)
            return retrived.value

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            retrived = self.storage[key]
            retrived.value = value
            self.list.move_to_head(retrived)

        else:

            node = Node(key=key, value=value)
            self.storage[key] = node
            self.list.add(node)
            self.size += 1

            if self.size > self.capacity:
                lastly_used = self.list.pop_tail()
                old_key = lastly_used.key
                del self.storage[old_key]

                self.size -= 1
