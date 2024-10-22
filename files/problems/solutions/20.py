class Solution:
    def isValid(self, s: str) -> bool:
        
        opening_pairs ="{(["
        closing_pairs ="}])"
        pairs ={"]":"[","}":"{",")":"("}
        stack =[]
        for bracket in s:
            if bracket in opening_pairs:
                stack.append(bracket)
            elif bracket in closing_pairs:
                if not len(stack):
                    return False
                last_element = stack.pop(len(stack)-1)
                if  pairs[bracket]== last_element:
                    continue
                else:
                    return False
            else: 
                return False
        return not len(stack)