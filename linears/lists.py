from typing import Optional


class Node:
    def __init__(self, key: int, value: int, next: Optional['Node'] = None):
        self.value = value
        self.key = key
        self.next = next


class LinkedList:

    def __init__(self, head: Node):
        self.head = head


class Bucket:

    def __init__(self, storage: Optional[LinkedList] = None):
        self.storage = storage


class MyHashMap:

    def __init__(self):
        self.storage = [Bucket() for i in range(729)]

    def __hash_it(self, key: int) -> int:
        return key % 729

    def put(self, key: int, value: int) -> None:
        bucket = self.__hash_it(key)

        current_bucket = self.storage[bucket]

        if current_bucket.storage is None:
            new_node = Node(key, value)
            linked_list = LinkedList(new_node)
            current_bucket.storage = linked_list

        else:
            runner = current_bucket.storage.head

            while runner.next is not None and runner.key != key:
                runner = runner.next

            if runner.key == key:
                runner.value = value
            else:
                runner.next = Node(key, value)

    def get(self, key: int) -> int:
        bucket = self.storage[self.__hash_it(key)]

        if bucket.storage is None:
            return -1

        runner = bucket.storage.head

        while runner is not None and runner.key != key:
            runner = runner.next

        if runner is not None:
            return runner.value

        return -1

    def remove(self, key: int) -> None:
        bucket = self.storage[self.__hash_it(key)]

        if bucket.storage is None:
            return

        slow = bucket.storage.head
        fast = bucket.storage.head

        # First element
        if fast is None and slow.key == key:
            bucket.storage = None

        # Looking for the right one
        while fast.key != key:

            fast = fast.next
            slow = fast

            if fast is None:
                break

        if fast is not None and fast.key == key:

            if fast == bucket.storage.head:
                bucket.storage.head = fast.next

                if bucket.storage.head is None:
                    bucket.storage = None

            else:
                slow.next = fast.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

if __name__ == '__main__':
    m = MyHashMap()
    m.put(1, 2)
    m.put(730, 10)
    m.put(10, 30)
    m.put(4, 20)

    print(m.get(1))
    print(m.get(730))
    print(m.get(10))
    print(m.get(4))

    m.remove(1)
    m.remove(730)
    m.remove(4)

    print("")

    print(m.get(1))
    print(m.get(730))
    print(m.get(10))
    print(m.get(4))



