# ref https://www.programiz.com/dsa/bubble-sort
from typing import Any, List
from sort import Sort
import operator


class Bubble(Sort):
    def __init__(self, data: List[Any] = ...) -> None:
        super().__init__(data)

    def sort(self) -> None:
        for x_index in range(len(self.data)):
            for y_index in range(len(self.data) - x_index - 1):

                operands = [self.data[y_index], self.data[y_index + 1]]
                if operator.gt(*operands) if self.direction else operator.le(*operands):
                    self.data[y_index], self.data[y_index + 1] = (
                        self.data[y_index + 1],
                        self.data[y_index],
                    )

        """Eg:
            [10,9,8,7,6,5,4,3,2,1]  # swapping iteratively makes the largest number to be at the end
            [9,8,7,6,5,4,3,2,1, 10]
            [8,7,6,5,4,3,2,1, 9,10]
            [7,6,5,4,3,2,1, 8.9,10]
            .
            .
            .
            [1,2,3,4,5,6,7,8,9,10]
        """
