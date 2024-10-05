from data_structures.stack.baseClass import Stack
from typing import Any
from data_structures.linked_list.singly_linked import SinglyLinkedList


class LinkedListStack(Stack):

    def __init__(self) -> None:
        self.stack = SinglyLinkedList()

    def push(self, value) -> Any:
        self.stack.add_value(value=value)

    def pop(self) -> Any:
        node = self.stack.get_tail()
        if node:
            self.stack.remove_tail()
            return node.value
        return None

    def is_empty(self) -> bool:
        return self.stack.size() == 0

    def peek(self) -> None:
        node = self.stack.get_tail()
        if node:
            return node.value
        return None

    def size(self) -> int:
        return self.stack.size()

    def clear(self) -> None:
        self.stack.delete()
