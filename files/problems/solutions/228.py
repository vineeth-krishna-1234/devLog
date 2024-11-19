class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not len(nums):
            return []
        range_start = nums[0]
        index = 1
        prev_value = nums[0]
        return_value = []
        while index < len(nums):
            if nums[index] != prev_value + 1:
                if range_start == prev_value:
                    return_value.append(str(prev_value))
                else:
                    return_value.append(f"{range_start}->{prev_value}")
                range_start = nums[index]
            prev_value = nums[index]
            index += 1
        else:
            if range_start == prev_value:
                return_value.append(str(prev_value))
            else:
                return_value.append(f"{range_start}->{prev_value}")
        return return_value
