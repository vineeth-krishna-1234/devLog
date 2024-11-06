class NumArray:

    def __init__(self, nums: List[int]):
        if not len(nums):
            return
        self.prefix_sum = [0] * len(nums)
        self.prefix_sum[0] = nums[0]
        for index in range(1, len(nums)):
            self.prefix_sum[index] = self.prefix_sum[index - 1] + nums[index]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]
