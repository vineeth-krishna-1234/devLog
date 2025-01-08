class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        max_len = 1
        index=1
        prev_element=nums[0]
        current_len =1
        while index <len(nums):
            if nums[index] ==prev_element+1:
                current_len+=1
            else:
                max_len = max(max_len,current_len)
                current_len=1
            prev_element= nums[index]
            index+=1
        else:
            max_len = max(max_len,current_len)
    
        return max_len