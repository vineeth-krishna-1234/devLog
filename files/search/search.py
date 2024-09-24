from abc import ABC, abstractmethod
from typing import List, Any


class Search(ABC):
    def __init__(self, data: List[Any] = []) -> None:
        self.data = data

    def get_data(self) -> List[Any]:
        return self.data

    def add_data(self, data: Any) -> None:
        self.data.append(data)

    def remove_element(self, target) -> None:
        index_value = self.search(target=target)
        if index_value != -1:
            del self.data[index_value]

    def remove_elements(self, target) -> None:
        indices = self.search_with_repetition(target=target)
        for index in sorted(indices, reverse=True):
            del self.data[index]

    @abstractmethod
    def search(self, target) -> int:
        # return the index of the first match
        pass

    @abstractmethod
    def search_with_repetition(self, target) -> List[int]:
        # returns the list of index of all matches
        pass
