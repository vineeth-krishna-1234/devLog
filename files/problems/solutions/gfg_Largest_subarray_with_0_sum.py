class Solution:
    def maxLen(self, arr):
        # code here
        
        hash_map = {}
        sum_value = 0
        max_len = 0
        
        for index in range(len(arr)):
            sum_value += arr[index]

            if not sum_value:
                max_len = max(max_len,index+1)
            
            if sum_value in hash_map:
                max_len = max(max_len,index-hash_map.get(sum_value))
            else:
                hash_map[sum_value]=index
        return max_len