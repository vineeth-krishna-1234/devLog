class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs = sorted(strs,key=lambda x : len(x))
        max_range = len(strs[0])

        index =0
        while index < max_range:
            if len(set(map(lambda x : x[index],strs))) ==1:
                index +=1
            else :
                return strs[0][:index]
        return strs[0][:index]