class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        index = 0
        records = {}
        while index < len(s):
            isomorphic_value = records.get(s[index], None)

            if isomorphic_value and isomorphic_value != t[index]:
                return False
            elif not isomorphic_value and t[index] in records.values():
                return False
            else:
                records[s[index]] = t[index]
            index += 1
        return True
