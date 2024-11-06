class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        prefix_sum = [0]
        suffix_sum = [0]

        temp = 0
        for i in nums:
            sum_value = i + temp
            prefix_sum.append(sum_value)
            temp = sum_value
        temp = 0
        for i in nums[::-1]:
            sum_value = i + temp
            suffix_sum.insert(0, sum_value)
            temp = sum_value

        for i in range(len(nums)):
            if prefix_sum[i] == suffix_sum[i + 1]:
                return i
        return -1


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        current_sum = 0

        for i in range(len(nums)):
            if current_sum == total - current_sum - nums[i]:
                return i
            current_sum = current_sum + nums[i]
        return -1
