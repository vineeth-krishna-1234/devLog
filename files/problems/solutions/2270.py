class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        if not(len(nums)):
            return 0
        total = sum(nums)
        current_sum = 0
        total_splits =0
        for element in nums[:-1]:
            current_sum +=element
            if  current_sum >= total-current_sum:
                total_splits+=1
        return total_splits