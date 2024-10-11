class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        pointer_x = m - 1
        pointer_y = n - 1
        placement_pointer = len(nums1) - 1

        while pointer_y >= 0:
            if pointer_x >= 0 and nums1[pointer_x] > nums2[pointer_y]:
                nums1[placement_pointer] = nums1[pointer_x]
                pointer_x -= 1
            else:
                nums1[placement_pointer] = nums2[pointer_y]
                pointer_y -= 1
            placement_pointer -= 1
