from search.baseClass import Search
from sort.bubble import Bubble
from typing import List, Any


class BinarySearch(Search):
    def __init__(self, data: List[Any] = []) -> None:
        # sor the
        sort_instance = Bubble(data=data)
        sort_instance.sort()
        super().__init__(data=sort_instance.get_data())
        self.data_length = len(data)

    def search(self, target, low=0, high=0) -> int:
        # return the index of the first match
        if low > high:
            return -1
        mid = (high + low) // 2

        if self.data[mid] == target:
            return mid
        elif self.data[mid] > target:
            return self.__divide_and_conquer(target=target, low=low, high=mid - 1)
        else:
            return self.__divide_and_conquer(target=target, low=mid + 1, high=high)

    def search_with_repetition(self, target, low=0, high=0) -> List[int]:

        if low > high:
            return []

        mid = (high + low) // 2

        if self.data[mid] == target:
            return (
                self.search_with_repetition(target=target, low=low, high=mid - 1)
                + [mid]
                + self.search_with_repetition(target=target, low=mid + 1, high=high)
            )

        elif self.data[mid] > target:
            return self.search_with_repetition(target=target, low=low, high=mid - 1)
        else:
            return self.search_with_repetition(target=target, low=mid + 1, high=high)
