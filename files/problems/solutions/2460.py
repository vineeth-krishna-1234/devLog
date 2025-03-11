class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                nums[index] = nums[index] * 2
                nums[index + 1] = 0
        answer = [0] * len(nums)
        index = 0

        for number in nums:
            if number:
                answer[index] = number
                index += 1

        return answer
