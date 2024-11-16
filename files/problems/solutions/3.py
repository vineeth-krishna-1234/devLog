class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_length = len(s)

        if not string_length:
            return 0

        start_index = end_index = longest_sub_string_length = 0
        hash_map = {}

        while end_index < string_length:

            current_element = s[end_index]
            element_index = hash_map.get(current_element, None)
            if element_index != None and (start_index <= element_index <= end_index):
                longest_sub_string_length = max(
                    longest_sub_string_length, end_index - start_index
                )
                start_index = element_index + 1
            else:
                hash_map[current_element] = end_index
                end_index += 1
        else:
            longest_sub_string_length = max(
                longest_sub_string_length, end_index - start_index
            )
        return longest_sub_string_length
