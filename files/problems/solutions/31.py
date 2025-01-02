class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        - Find pivot , the element that breaks the strictly decreasing from the end
        - Find successor , the element from the end that is greater than the pivot
        - Swap the pivot and successor
        - reverse all the element after the pivot index
        """
        # find pivot

        pivot_index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot_index = i
                break

        if pivot_index == -1:
            nums = nums.reverse()
            return

        # find successor
        successor_index = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[pivot_index]:
                successor_index = i
                break

        # swap pivot and successor
        nums[pivot_index], nums[successor_index] = (
            nums[successor_index],
            nums[pivot_index],
        )
        nums[pivot_index + 1 :] = nums[pivot_index + 1 :][::-1]
