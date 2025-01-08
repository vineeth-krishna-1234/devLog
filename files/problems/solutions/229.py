from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict(int)

        return_value = set()

        threshold = len(nums) / 3

        for element in nums:
            hash_map[element] = hash_map[element] + 1
            if hash_map[element] > threshold:
                return_value.add(element)
        return list(return_value)
