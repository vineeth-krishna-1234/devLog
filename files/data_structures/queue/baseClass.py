from abc import ABC, abstractmethod
from typing import Any


class Queue:

    @abstractmethod
    def enqueue(self, value) -> Any:
        pass

    @abstractmethod
    def dequeue(self) -> None:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def peek(self) -> None:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
