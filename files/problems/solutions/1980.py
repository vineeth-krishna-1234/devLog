class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        string_len = len(nums[0])

        def bt(current_string):
            current_string_len = len(current_string)
            if current_string_len == string_len and (current_string not in nums):
                return current_string
            if current_string_len > string_len:
                return None
            output_1 = bt(current_string + "0")
            return bt(current_string + "1") if not output_1 else output_1

        return bt("")
