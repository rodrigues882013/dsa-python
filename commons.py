from abc import abstractmethod
from enum import Enum
from typing import List, Optional


class Color(Enum):
    RED = 1
    BLACK = 0


class ListNode:
    def __init__(self, value, next_: Optional['ListNode'] = None, previous: Optional['ListNode'] = None):
        self.value = value
        self.next = next_
        self.prev = previous


class Node:
    def __init__(self, value: int, color: Color = Color.BLACK, parent: Optional['Node'] = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color


class NTreeNode:
    def __init__(self, value: int,
                 color: Color = Color.BLACK,
                 parent: Optional['NTreeNode'] = None,
                 children: List[Optional['NTreeNode']] = None):
        self.value = value
        self.children = children
        self.parent = parent
        self.color = color


class Tree:
    def __init__(self):
        self.root = None

    @abstractmethod
    def insert(self, value: int):
        pass

    def get_in_order(self) -> List[int]:
        if self.root is None:
            return []

        ans = []

        def helper(node: Node):

            if node is not None:
                helper(node.left)
                ans.append(node.value)
                helper(node.right)

        helper(self.root)
        return ans

    def get_pre_order(self) -> List[int]:
        if self.root is None:
            return []

        ans = []

        def helper(node: Node):

            if node is not None:
                ans.append(node.value)
                helper(node.left)
                helper(node.right)

        helper(self.root)
        return ans

    def get_post_order(self) -> List[int]:
        if self.root is None:
            return []

        ans = []

        def helper(node: Node):

            if node is not None:
                helper(node.left)
                helper(node.right)
                ans.append(node.value)

        helper(self.root)
        return ans
