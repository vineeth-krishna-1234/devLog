class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        array_len = len(nums)
        for index in range(array_len):

            right = nums[index - 1] if index else float("-inf")
            left = nums[index + 1] if index != array_len - 1 else float("-inf")

            if left < nums[index] and nums[index] > right:
                return index
        return 0
