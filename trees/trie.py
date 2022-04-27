from commons import TrieNode


class Trie:
    def __init__(self):
        self.__root = TrieNode()

    # Time complexity: O(n), where n is the length of word
    # Space complexity: O(1), which has a constant time regardless be the size of word
    def add(self, word):
        current = self.__root

        for letter in word:
            node = current.children.get(letter)
            if not node:
                node = TrieNode()
                current.children[letter] = node
            current = node

        current.is_end = True

    # Time complexity: O(n), where n is the length of word
    # Space complexity: O(1), which has a constant time regardless be the size of word
    def search(self, word) -> bool:
        current = self.__root

        for letter in word:
            node = current.children.get(letter)

            if not node:
                return False

            current = node

        return current.is_end

    def search_by_prefix(self, word) -> bool:
        current = self.__root

        for letter in word:
            node = current.children.get(letter)

            if not node:
                return False

            current = node

        return True


def main():
    t = Trie()
    t.add("Felipe")
    t.add("Fernanda")
    t.add("Lilia")

    print(t.search_by_prefix(""))


if __name__ == '__main__':
    main()
