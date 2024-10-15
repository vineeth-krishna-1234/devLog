class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        if len(haystack) < len(needle):
            return -1
        
        haystack_index = 0
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        while haystack_index <= haystack_length - needle_length:
            if haystack[haystack_index] == needle[0]:
                temp = haystack_index
                needle_index = 0
                
                while temp < haystack_length and needle_index < needle_length:
                    if haystack[temp] != needle[needle_index]:
                        break
                    temp += 1
                    needle_index += 1
                
                if needle_index == needle_length:
                    return haystack_index
            
            haystack_index += 1
        
        return -1
