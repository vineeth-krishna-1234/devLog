from search.baseClass import Search
from typing import List, Any


class LinearSearch(Search):
    def __init__(self, data: List[Any] = []) -> None:
        super().__init__(data=data)

    def search(self, target) -> int:
        # return the index of the first match
        for index in range(len(self.data)):
            if self.data[index] == target:
                return index
        return -1

    def search_with_repetition(self, target) -> List[int]:
        # returns the list of index of all matches
        indices = []
        for index in range(len(self.data)):
            if self.data[index] == target:
                indices.append(index)
        return indices
