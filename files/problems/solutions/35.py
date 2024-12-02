class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    return binary_search(left, mid)
                return binary_search(mid + 1, right)
            else:
                return left

        return binary_search(0, len(nums))
