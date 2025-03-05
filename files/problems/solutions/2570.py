from collections import defaultdict


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:

        hash_map = defaultdict(int)

        for element in nums1:
            hash_map[element[0]] = hash_map[element[0]] + element[-1]
        for element in nums2:
            hash_map[element[0]] = hash_map[element[0]] + element[-1]

        answer = list(map(list, hash_map.items()))
        answer.sort()
        return answer
