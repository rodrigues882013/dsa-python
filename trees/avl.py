import os
from typing import Optional
from commons import Node, Tree

"""
Insert -> Best Case: O(log N), Worst Case: O(log N)
Delete -> Best Case: O(log N), Worst Case: O(log N)
Search
"""

class AVLTree(Tree):

    @staticmethod
    def __left_rotate(node: Node) -> Node:

        subtree = node.right
        tmp = subtree.left

        subtree.left = node
        node.right = tmp

        return subtree

    @staticmethod
    def __right_rotate(node: Node) -> Node:
        subtree = node.left
        tmp = subtree.right

        subtree.right = node
        node.left = tmp

        return subtree

    def __do_balance(self, node: Node, data: int) -> Node:
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        balance = left_height - right_height

        if balance < -1:
            if data < node.right.value:

                # right-left
                node.right = self.__right_rotate(node.right)
                node = self.__right_rotate(node)

            else:

                # left
                node = self.__left_rotate(node)

        elif balance > 1:
            if data > node.left.value:

                # left-right
                node.left = self.__left_rotate(node.left)
                node = self.__left_rotate(node)

            else:
                # right
                node = self.__right_rotate(node)

        return node

    def __insert(self, n: Node, value: int) -> Node:
        if n is None:
            return Node(value)

        if value > n.value:

            if n.right is None:
                n.right = Node(value)

            else:
                n.right = self.__insert(n.right, value)

        elif value < n.value:

            if n.left is None:
                n.left = Node(value)

            else:
                n.left = self.__insert(n.left, value)
        else:
            os.abort()

        return self.__do_balance(n, value)

    def insert(self, value: int):
        self.root = self.__insert(self.root, value)

    def get_height(self, node: Optional[Node]) -> int:

        if node is None:
            return 0

        elif node.left is None and node.right is None:
            return 1

        elif node.left is None:
            return 1 + self.get_height(node.right)

        elif node.right is None:
            return 1 + self.get_height(node.left)

        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))


if __name__ == '__main__':
    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)

    print(tree.get_in_order())
    print(tree.get_pre_order())
    print(tree.get_post_order())
