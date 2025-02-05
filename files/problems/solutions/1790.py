class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mis_match_set = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mis_match_set.append([s1[i], s2[i]])

        if not len(mis_match_set):
            return True
        elif len(mis_match_set) != 2:
            return False
        elif (
            mis_match_set[0][1] == mis_match_set[1][0]
            and mis_match_set[1][1] == mis_match_set[0][0]
        ):
            return True
        return False
