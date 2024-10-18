class Solution:
    def isHappy(self, n: int) -> bool:
        history_mapping = {}
        while True:
            if n == 1:
                return True
            if history_mapping.get(n, False):
                return False
            temp = 0
            for char in str(n):
                temp += pow(int(char), 2)
            history_mapping[n] = temp
            n = temp
