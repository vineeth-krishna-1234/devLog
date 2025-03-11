class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        left_index = 0
        hash_value = [0] * 3
        answer = 0

        for index in range(len(s)):

            hash_value[ord(s[index]) - ord("a")] += 1
            while hash_value[0] and hash_value[1] and hash_value[2]:
                answer += len(s) - index
                hash_value[ord(s[left_index]) - ord("a")] -= 1
                left_index += 1

        return answer
