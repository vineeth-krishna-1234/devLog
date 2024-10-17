class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        pattern_record = {}
        s = s.strip().split()

        if len(pattern) != len(s):
            return False

        index = 0
        while index < len(pattern):
            pattern_mapping = pattern_record.get(pattern[index], None)
            if (pattern_mapping and pattern_mapping != s[index]) or (
                not pattern_mapping and s[index] in pattern_record.values()
            ):
                return False
            else:
                pattern_record[pattern[index]] = s[index]
            index += 1
        return True
