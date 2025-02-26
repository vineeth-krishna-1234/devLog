class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)
        stack = []

        for index, element in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < element:
                day_index = stack.pop()
                answer[day_index] = index - day_index
            stack.append(index)

        return answer
