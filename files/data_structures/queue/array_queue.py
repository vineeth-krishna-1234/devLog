from data_structures.queue.baseClass import Queue
from typing import Any


class ArrayQueue(Queue):

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, value) -> None:
        self.queue.append(value)

    def dequeue(self) -> Any:
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def peek(self) -> None:
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self) -> int:
        return len(self.queue)

    def clear(self) -> None:
        self.queue = []
