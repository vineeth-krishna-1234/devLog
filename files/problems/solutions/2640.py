class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        
        if not len(nums):
            return []
        
        max_value = nums[0]
        prefix_sum =[2*nums[0]]
        for index in range(1,len(nums)):
            max_value =max(max_value,nums[index])
            prefix_sum.append(nums[index] + max_value+prefix_sum[index-1])
        return prefix_sum