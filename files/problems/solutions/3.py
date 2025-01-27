class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        start_index = 0
        max_len = 0
        for end_index in range(len(s)):

            element_at_index = s[end_index]
            if element_at_index in hash_map:
                start_index = max(start_index, hash_map[element_at_index] + 1)
            hash_map[element_at_index] = end_index
            max_len = max(max_len, end_index - start_index + 1)
        return max_len
