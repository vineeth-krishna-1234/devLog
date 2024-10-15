class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        x_index =0
        y_index =len(s)-1

        while x_index <y_index:
            if not s[x_index].isalnum():
                x_index+=1
                continue
            if not s[y_index].isalnum():
                y_index-=1
                continue
            if not s[y_index]==s[x_index]:
                return False
            x_index+=1
            y_index-=1
        return True