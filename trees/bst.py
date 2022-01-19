from commons import Node, Tree


class BSTree(Tree):

    def __insert(self, root: Node, value: int) -> Node:
        if root is None:
            return Node(value)

        elif value > root.value:
            root.right = self.__insert(root.right, value)

        elif value < root.value:
            root.left = self.__insert(root.left, value)

        else:
            raise Exception('Node already allocated')

        return root

    def insert(self, value: int):
        self.root = self.__insert(self.root, value)


if __name__ == '__main__':
    tree = BSTree()
    tree.insert(3)
    tree.insert(3)
    tree.insert(4)
    tree.insert(1)
    tree.insert(100)
