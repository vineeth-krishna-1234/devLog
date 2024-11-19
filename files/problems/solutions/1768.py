class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        index = 0 
        max_len = min(len(word1),len(word2))
        return_string =""
        while index < max_len:
            return_string+=word1[index]+word2[index]
            index+=1
        
        if len(word1)>index:
            return_string+=word1[index:]
        if len(word2)>index:
            return_string+= word2[index:]
        
        return return_string