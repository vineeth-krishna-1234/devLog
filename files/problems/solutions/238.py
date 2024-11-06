class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = [1] * len(nums)

        product_value = 1
        for i in range(len(nums)):
            product_array[i] = product_value
            product_value = product_value * nums[i]
        product_value = 1
        for i in range(len(nums) - 1, -1, -1):
            product_array[i] = product_value * product_array[i]
            product_value = product_value * nums[i]

        return product_array
