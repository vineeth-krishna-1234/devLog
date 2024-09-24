from abc import ABC, abstractmethod
from typing import List, Any


class Sort(ABC):
    def __init__(self, data: List[Any] = []) -> None:
        self.data = data
        self.direction = True

    def get_data(self) -> List[Any]:
        return self.data

    def add_data(self, data: Any) -> None:
        self.data.append(data)

    def remove_element(self, target) -> None:
        index_value = self.search(target=target)
        if index_value != -1:
            del self.data[index_value]

    def get_array_lenght(self):
        return len(self.data)

    def remove_elements(self, target) -> None:
        indices = self.search_with_repetition(target=target)
        for index in sorted(indices, reverse=True):
            del self.data[index]

    def set_direction(self, direction=bool):
        self.direction = direction

    @abstractmethod
    def sort(self) -> int:
        # return the index of the first match
        pass
