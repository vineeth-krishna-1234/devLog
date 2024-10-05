from data_structures.linked_list.singly_linked import SinglyLinkedList
from data_structures.queue.baseClass import Queue
from typing import Any


class LinkedListQueue(Queue):

    def __init__(self) -> None:
        self.queue = SinglyLinkedList()

    def enqueue(self, value) -> None:
        self.queue.add_value(value=value)

    def dequeue(self) -> Any:
        node = self.queue.get_head()
        if node:
            self.queue.remove_head()
            return node.value
        return None

    def is_empty(self) -> bool:
        return self.queue.get_head() == None

    def peek(self) -> None:
        if self.queue.get_head():
            return self.queue.value_at_index(target=0)
        return None

    def size(self) -> int:
        return self.queue.size()

    def clear(self) -> None:
        self.queue.delete()
