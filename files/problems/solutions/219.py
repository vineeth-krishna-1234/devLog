from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_records ={}
        index = 0
        while index < len(nums):
            already_present = index_records.get(nums[index],None)
            if already_present == None:
                index_records[nums[index]]=index
                index+=1
                continue
            if abs(index - already_present) <= k:
                return True
            else:
                index_records[nums[index]]=index
            index+=1
        return False