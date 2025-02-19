class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        final_list = []

        def recursive_function(open_count, close_count, current_string):

            if open_count == n and close_count == n:
                final_list.append(current_string)
                return
            if open_count < n:
                recursive_function(open_count + 1, close_count, current_string + "(")
            if close_count < open_count and close_count < n:
                recursive_function(open_count, close_count + 1, current_string + ")")

        recursive_function(0, 0, "")
        return final_list
