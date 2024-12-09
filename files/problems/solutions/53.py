class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        total_maximum = current_sum = nums[0]

        # kadane 's algorithm
        # the maximum sum ending in the current element is the maximum of either the current element or the sum of all previous elements + current element
        for element in nums[1:]:
            current_sum = max(current_sum + element, element)
            total_maximum = max(total_maximum, current_sum)
        return total_maximum
