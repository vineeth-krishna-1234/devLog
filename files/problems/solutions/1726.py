import math
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        hash_map = defaultdict(int)

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                hash_map[product] += 1

        pairs = 0
        for i in hash_map.values():
            pairs += math.comb(i, 2)

        return pairs * 8
