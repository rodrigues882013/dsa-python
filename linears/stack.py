import math


class Node:
    def __init__(self, value=-math.inf, prev=None):
        self.value = value
        self.prev = prev


class MaxStack:

    def __init__(self):
        self.head = None
        self.max_head = None
        self.maximum = None

    def push(self, x: int) -> None:
        new_node = Node(x, None)
        new_max_node = Node(x, None)

        if self.head is None:
            self.head = new_node
            self.head.max = x
            new_max_node.value = x
            self.max_head = new_max_node

        else:
            new_node.prev = self.head
            new_max_node.prev = self.max_head

            if self.max_head.value <= x:
                new_max_node.value = x
            else:
                new_max_node.value = self.max_head.value

            self.head = new_node
            self.max_head = new_max_node

    def pop(self) -> int:

        popped = self.head
        popped_value = popped.value
        self.head = self.head.prev
        popped = None

        popped_from_max = self.max_head
        self.max_head = self.max_head.prev
        popped_from_max = None

        return popped_value

    def top(self) -> int:
        return self.head.value

    def peekMax(self) -> int:
        return self.max_head.value

    def popMax(self) -> int:
        maxi = self.peekMax()
        buffer = MaxStack()

        while self.top() != maxi:
            buffer.push(self.pop())

        self.pop()

        while buffer.head is not None:
            self.push(buffer.pop())
        return maxi


if __name__ == '__main__':
    m = MaxStack()
    m.push(5)
    m.push(1)
    m.push(-5)

    print(m.popMax())
    print(m.popMax())
    print(m.top())

