class Solution:

    def searchArray(self,array,target):
        for element in array:
            if element ==target:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0]<=target<=row[-1]:
                return self.searchArray(row,target)
        return False