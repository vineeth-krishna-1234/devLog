class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        return_array = []
        letters = ["a", "b", "c"]

        def stringGenerator(happy_string):
            happy_string_len = len(happy_string)
            if happy_string_len == n:
                return_array.append(happy_string)
                return

            for letter in letters:
                if happy_string_len and happy_string[-1] == letter:
                    continue
                stringGenerator(happy_string + letter)

        stringGenerator("")
        if len(return_array) < k:
            return ""
        return return_array[k - 1]
