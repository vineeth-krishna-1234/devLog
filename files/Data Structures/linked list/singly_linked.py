from typing import Any, List


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_value(self, value) -> None:
        new_node = Node(value=value)
        tail_node = self.get_tail()
        if tail_node:
            tail_node.next = new_node
        else:
            self.head = new_node

    def remove_value(self, target) -> None:
        # remove the first occuring node with the value
        if self.head and self.head.value == target:
            self.head = self.head.next
            return

        previous_node = None
        cursor_ = self.head

        while cursor_:
            if cursor_.value == target:
                previous_node.next = previous_node.next.next
                return
            previous_node = cursor_
            cursor_ = cursor_.next

    def remove_tail(self) -> None:
        cursor_ = self.head
        while cursor_ and cursor_.next and cursor_.next.next:
            cursor_ = cursor_.next
        cursor_.next.next = None

    def remove_head(self) -> None:
        if self.head:
            self.head = self.head.next

    def remove_index(self, target) -> None:
        # remove the node with index , index starts with 0
        if target == 0 and self.head:
            self.head = self.head.next
            return

        cursor_ = self.head
        index = 0
        while cursor_:
            if index == target - 1:
                cursor_.next = cursor_.next.next if cursor_.next else None
                return

    def get_value_list(self) -> List[Any]:
        # get the values of all nodes as a list
        return_value = []
        cursor_ = self.head
        while cursor_:
            return_value.append(cursor_.value)
            cursor_ = cursor_.next
        return return_value

    def value_at_index(self, target) -> Any:
        index = 0
        cursor_ = self.head
        while cursor_:
            if index == target:
                return cursor_.value
            cursor_ = cursor_.next
            index += 1
        return None

    def search(self, target) -> int:
        cursor_ = self.head
        index = 0
        while cursor_:
            if cursor_.value == target:
                return index
            cursor_ = cursor_.next
            index += 1
        return -1

    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        cursor_ = self.head
        while cursor_ and cursor_.next:
            cursor_ = cursor_.next
        return cursor_

    def reverse(self) -> None:
        cursor_ = self.head
        previous_node = None
        while cursor_:
            temp_cursor = cursor_.next
            cursor_.next = previous_node
            previous_node = cursor_
            cursor_ = temp_cursor
        self.head = previous_node

    def count(self, target) -> int:
        count = 0
        cursor_ = self.head
        while cursor_:
            if cursor_.value == target:
                count += 1
            cursor_ = cursor_.next
        return count

    def remove_values(self, target) -> None:
        # remove all the nodes matching the value
        pass

    def sort(self) -> None:
        pass

    def remove_duplicates(self) -> None:
        pass

    def rotate_list(self) -> None:
        pass
