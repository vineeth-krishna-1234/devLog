class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        element_index = {}
        row_len = len(mat)
        col_len = len(mat[0])

        row_frequency = [0] * row_len
        col_frequency = [0] * col_len

        for row in range(row_len):
            for col in range(col_len):
                element_index[mat[row][col]] = [row, col]

        for index in range(len(arr)):
            row_index, col_index = element_index[arr[index]]
            row_frequency[row_index] = row_frequency[row_index] + 1
            col_frequency[col_index] = col_frequency[col_index] + 1
            # print(row_frequency,col_frequency,arr[index],index)
            if (col_len == row_frequency[row_index]) or (
                row_len == col_frequency[col_index]
            ):
                return index
        return -1
