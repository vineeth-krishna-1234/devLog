# ref https://www.programiz.com/dsa/selection-sort

from typing import Any, List
from sort import Sort
import operator


class Selection(Sort):
    def __init__(self, data: List[Any]) -> None:
        super().__init__(data)

    def sort(self) -> None:
        for x_index in range(self.get_array_lenght()):
            value_index = x_index
            for y_index in range(x_index + 1, self.get_array_lenght()):
                operands = [self.data[y_index], self.data[value_index]]
                if operator.lt(*operands) if self.direction else operator.gt(*operands):
                    value_index = y_index
            self.data[value_index], self.data[x_index] = (
                self.data[x_index],
                self.data[value_index],
            )

        """__Example__
        [54, 46, 29, 67, 66, 70, 71, 85, 89, 90, 67] > find the minimum number and swap it with the starting indes
        [29, 46, 54, 67, 66, 70, 71, 85, 89, 90, 67]
        [29, 46, 54, 67, 66, 70, 71, 85, 89, 90, 67]
        [29, 46, 54, 67, 66, 70, 71, 85, 89, 90, 67]
        .
        .
        .
        [29, 46, 54, 66, 67, 67, 70, 71, 85, 89, 90]
        """
