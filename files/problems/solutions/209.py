class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        array_len = len(nums)
        start_index = window_sum = 0
        min_sub_array_length = array_len + 1
        for end_index in range(array_len):
            window_sum += nums[end_index]
            while start_index < array_len and window_sum >= target:
                min_sub_array_length = min(
                    min_sub_array_length, end_index - start_index + 1
                )
                window_sum -= nums[start_index]
                start_index += 1
        return min_sub_array_length if min_sub_array_length <= array_len else 0
