from data_structures.stack.baseClass import Stack
from typing import Any


class ArrayStack(Stack):

    def __init__(self) -> None:
        self.stack = []

    def push(self, value) -> Any:
        self.stack.append(value)

    def pop(self) -> Any:
        if self.is_empty():
            return None
        return self.stack.pop(self.size()-1)

    def is_empty(self) -> bool:
        return len(self.stack)== 0

    def peek(self) -> None:
        if self.is_empty():
            return None
        return self.stack[self.size()-1]

    def size(self) -> int:
        return len(self.stack)

    def clear(self) -> None:
        self.stack = []
