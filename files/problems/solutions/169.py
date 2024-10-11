class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        current_element = nums[0]
        count = 0

        for element in nums:
            if count >= len(nums)/2:
                return current_element
            if element==current_element:
                count+=1
            else:
                current_element = element
                count=1
        return current_element
            