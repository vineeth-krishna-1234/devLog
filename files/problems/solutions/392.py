class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sequence_index = 0
        sub_sequence_index = 0
        while sequence_index < len(t) and sub_sequence_index < len(s):
            if t[sequence_index] == s[sub_sequence_index]:
                sub_sequence_index += 1
            sequence_index += 1
        return sub_sequence_index == len(s)
