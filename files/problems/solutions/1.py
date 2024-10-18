class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_records ={}

        index =0
        while index < len(nums):
            required_pair = target - nums[index]
            other_index = pair_records.get(nums[index],None)
            if other_index!=None:
                return [other_index,index]
            else:
                pair_records[required_pair]=index
            index+=1
        return False