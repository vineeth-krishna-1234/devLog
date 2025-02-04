class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        start_index=current_sum=iterator=max_sum=0
        while iterator < len(nums):
            if not iterator:
                current_sum+=nums[iterator]
            else:
                if nums[iterator]-nums[iterator-1]>0:
                    current_sum+=nums[iterator]
                else:
                    current_sum=nums[iterator]
            max_sum = max(max_sum,current_sum)
            iterator+=1
        return max_sum
