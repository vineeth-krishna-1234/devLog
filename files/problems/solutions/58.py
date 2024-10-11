class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s[::-1].strip(" ")
        count =0
        for char in s:
            if char ==" ":
                return count
            else : 
                count+=1
        return count