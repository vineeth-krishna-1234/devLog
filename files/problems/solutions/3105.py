class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        current_length_inc = 0
        current_length_dec = 0
        max_length = 0

        for i in range(1, len(nums)):
            difference = nums[i] - nums[i - 1]
            if difference > 0:
                current_length_inc += 1
                current_length_dec = 0
            elif difference < 0:
                current_length_dec += 1
                current_length_inc = 0
            else:
                current_length_inc = 0
                current_length_dec = 0
            max_length = max(max_length, current_length_inc, current_length_dec)
        return max_length + 1
