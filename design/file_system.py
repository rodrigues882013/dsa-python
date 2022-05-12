from typing import List

"""
Just a utility function
"""


def get_directory_list_from_given_path(path):
    return path.split('/')[1:]


"""
The file node entity
"""


class FileNode:

    def __init__(self):
        self.children = {}
        self.contents = ""


"""
A python file system emulator, just to practice some DSA concepts
"""


class FileSystem:

    def __init__(self):
        self.root = FileNode()

    def ls(self, path: str) -> List[str]:
        items = []

        if path == '/':
            items = list(self.root.children.keys())
            items.sort()
            return items

        path = get_directory_list_from_given_path(path)
        current = self.root

        for name in path:
            node = current.children.get(name)

            if node is None:
                break

            current = node

        if current.contents != "":
            items.append(path[-1])

        else:
            items.extend(current.children.keys())

        items.sort()
        return items

    def mkdir(self, path: str) -> None:
        path = path.split("/")[1:]

        current = self.root

        for letter in path:
            node = current.children.get(letter)

            if node is None:
                node = FileNode()
                current.children[letter] = node
            current = node

    def add_content_to_file(self, file_path: str, content: str) -> None:
        path = get_directory_list_from_given_path(file_path)
        current = self.root

        for letter in path:
            node = current.children.get(letter)

            if node is None:
                node = FileNode()
                current.children[letter] = node
            current = node

        current.contents += content

    def read_content_from_file(self, file_path: str) -> str:
        path = get_directory_list_from_given_path(file_path)
        current = self.root

        for name in path:
            node = current.children.get(name)

            if node is None:
                break
            current = node

        return current.contents
