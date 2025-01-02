class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        placement_index = len(nums1)-1 
        while n and m:
            if nums1[m-1]>nums2[n-1]:
                nums1[placement_index]=nums1[m-1]
                m-=1
                placement_index-=1
            else:
                nums1[placement_index]=nums2[n-1]
                n-=1
                placement_index-=1
        while n:
            nums1[placement_index]=nums2[n-1]
            n-=1
            placement_index-=1
        while m:
            nums1[placement_index]=nums1[m-1]
            m-=1
            placement_index-=1


