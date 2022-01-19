import os
from typing import Optional

from commons import Tree, Node, Color


class RBLTree(Tree):
    def __left_rotate(self, node: Node) -> None:

        right: Node = node.right
        node.right = right.left

        if node.right is not None:
            node.right.parent = node

        right.parent = node.parent

        if node.parent is None:
            self.root = right

        elif node == node.parent.left:
            node.parent.left = right

        else:
            node.parent.right = right

        right.left = node
        node.parent = right

    def __right_rotate(self, node: Node) -> None:

        left: Node = node.left
        node.left = left.right

        if node.left is not None:
            node.left.parent = node

        left.parent = node.parent

        if node.parent is None:
            self.root = left

        elif node == node.parent.left:
            node.parent.left = left

        else:
            node.parent.right = left

        left.right = node
        node.parent = left

    def __fix_colors(self, root: Node, n: Node) -> None:

        # If parent is black or is root, there isn't nothing to do
        while n != root and n.color != Color.BLACK and n.parent.color == Color.RED:

            parent = n.parent
            grand_parent = n.parent.parent

            if parent == grand_parent.left:
                parent_sibling = grand_parent.right

                if parent_sibling is not None and parent_sibling.color == Color.RED:

                    # Recolor new node's parent and new node's sibling's parent
                    grand_parent.color = Color.RED
                    parent.color = Color.BLACK
                    parent_sibling.color = Color.BLACK
                    n = grand_parent

                else:

                    if n == parent.right:
                        self.__left_rotate(parent)
                        n = parent
                        parent = n.parent

                    self.__right_rotate(grand_parent)
                    tmp = parent.color
                    parent.color = grand_parent.color
                    grand_parent.color = tmp
                    n = parent
            else:
                parent_sibling = grand_parent.left

                if parent_sibling is not None and parent_sibling.color == Color.RED:
                    grand_parent.color = Color.RED
                    parent.color = Color.BLACK
                    parent_sibling.color = Color.BLACK
                    n = grand_parent
                else:
                    if n == parent.left:
                        self.__right_rotate(parent)
                        n = parent
                        parent = n.parent

                    self.__left_rotate(grand_parent)
                    tmp = parent.color
                    parent.color = grand_parent.color
                    grand_parent.color = tmp
                    n = parent

        root.color = Color.BLACK

    def __insert(self, root: Optional[Node], new_node: Node) -> Node:

        if root is None:
            return new_node

        if new_node.value > root.value:

            if root.right is None:
                new_node.parent = root
                root.right = new_node
            else:
                root.right = self.__insert(root.right, new_node)

        elif new_node.value < root.value:

            if root.left is None:
                new_node.parent = root
                root.left = new_node

            else:
                root.left = self.__insert(root.left, new_node)
        else:
            os.abort()

        return root

    def insert(self, value: int):
        # (1) If the tree is empty create the new node as root with color BLACK
        new_node: Node

        if self.root is None:
            new_node = Node(value, Color.BLACK)
            self.root = self.__insert(self.root, new_node)

        else:
            # (2) Otherwise perform a BST insertion with a node being colored as a RED
            new_node = Node(value, Color.RED)
            self.root = self.__insert(self.root, new_node)

        # After perform bst insertion, lets check the RBL properties and fix them if necessary
        self.__fix_colors(self.root, new_node)

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
    tree = RBLTree()
    tree.insert(10)
    tree.insert(18)
    tree.insert(7)
    tree.insert(15)
    tree.insert(16)
    tree.insert(30)
    tree.insert(25)
    tree.insert(40)
    tree.insert(60)
    tree.insert(2)
    tree.insert(1)
    tree.insert(70)
    print(tree.get_in_order())
