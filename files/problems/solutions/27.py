class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        pointer_x =0 # +ve traversal
        pointer_y = len(nums)-1 # -ve traversal
        while pointer_x<=pointer_y:
            if nums[pointer_y]==val:
                pointer_y-=1
                continue
            if nums[pointer_x]==val:
                nums[pointer_x]=nums[pointer_y]
                pointer_y-=1
            pointer_x+=1
        return pointer_x