class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        if k < 0:
            code = code[::-1]
        window_size = abs(k)
        return_value = []
        window_sum = sum(code[:window_size])
        array_len = len(code)

        for i in range(len(code)):
            window_sum = window_sum - code[i] + code[(i + window_size) % array_len]
            return_value.append(window_sum)
        return return_value if k > 0 else return_value[::-1]
