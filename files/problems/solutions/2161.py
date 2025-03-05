class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        less_than_pivot = []
        greater_than_pivot = []
        equal_to_pivot = []

        for number in nums:
            if number < pivot:
                less_than_pivot.append(number)
            elif number > pivot:
                greater_than_pivot.append(number)
            else:
                equal_to_pivot.append(number)

        return less_than_pivot + equal_to_pivot + greater_than_pivot
