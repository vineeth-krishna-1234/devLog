class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for element in tokens:
            if len(element) > 1 or element.isdigit():
                stack.append(int(element))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(eval(f"{b}{element}{a}")))
        return stack[0]
