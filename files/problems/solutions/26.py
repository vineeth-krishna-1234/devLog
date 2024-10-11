class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer_x = 0
        pointer_y = 1
        while pointer_y<len(nums):

            if nums[pointer_x]!=nums[pointer_y]:
                nums[pointer_x+1]=nums[pointer_y]
                pointer_x+=1
            pointer_y+=1
        return pointer_x+1
        
