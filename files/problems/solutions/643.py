class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) < k:
            return
        window = sum(nums[:k])
        max_value = window
        for i in range(len(nums) - k):
            window = window - nums[i] + nums[i + k]
            max_value = max(max_value, window)
        return max_value / k
