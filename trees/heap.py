from typing import List

from commons import Tree


class Heap(Tree):

    def __init__(self):
        super().__init__()
        self.__storage = []
        self.__size = 0

    def insert(self, value: int):
        self.__storage.append(value)
        self.__size += 1

        if self.__size > 1:
            self.__bubble_up(self.__size - 1)

    def pop(self):
        self.__storage[0] = self.__storage[self.__size - 1]
        self.__size -= 1

        if self.__size == 0:
            self.__storage = []

        self.__bubble_down(0)

    def __bubble_up(self, last_index: int):
        parent_index = last_index // 2

        if self.__storage[last_index] > self.__storage[last_index]:
            tmp = self.__storage[last_index]
            self.__storage[last_index] = self.__storage[parent_index]
            self.__storage[parent_index] = tmp
            self.__bubble_up(parent_index)

    def __bubble_down(self, first_index: int):

        # Just two elements in list generate a special treatment
        if self.__size == 2:
            tmp = self.__storage[1]

            if tmp > self.__storage[0]:
                self.__storage[1] = self.__storage[0]
                self.__storage[0] = tmp

            return

        left_child = first_index * 2
        right_child = (first_index * 2) + 1

        if left_child > self.__size - 2 or right_child > self.__size - 2:
            return

        if self.__storage[first_index] > self.__storage[left_child + 1] and self.__storage[first_index] > \
                self.__storage[right_child + 1]:
            return

        if self.__storage[left_child + 1] >= self.__storage[right_child + 1]:
            tmp = self.__storage[first_index]
            self.__storage[first_index] = self.__storage[left_child + 1]
            self.__storage[left_child + 1] = tmp
            self.__bubble_down(left_child + 1)

        elif self.__storage[left_child + 1] < self.__storage[right_child + 1]:
            tmp = self.__storage[first_index]
            self.__storage[first_index] = self.__storage[right_child + 1]
            self.__storage[right_child + 1] = tmp
            self.__bubble_down(right_child + 1)

    def get_max(self) -> int:
        return self.__storage[0]

    def get_in_order(self) -> List[int]:
        print("Don't supported")
        return []

    def get_pre_order(self) -> List[int]:
        print("Don't supported")
        return []

    def get_post_order(self) -> List[int]:
        print("Don't supported")
        return []
