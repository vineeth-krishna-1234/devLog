class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_len = len(matrix[0])
        col_len = len(matrix)
        rows = [0] * row_len
        cols = [0] * col_len
        for row_index in range(row_len):
            for col_index in range(col_len):
                if not matrix[col_index][row_index]:
                    rows[row_index] = cols[col_index] = 1

        for row_index in range(row_len):
            for col_index in range(col_len):
                if cols[col_index] or rows[row_index]:
                    matrix[col_index][row_index] = 0
