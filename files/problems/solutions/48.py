class Solution:

    def turn_up_side_down(self, matrix):
        row = column = len(matrix)
        for row_index in range(row // 2):
            for column_index in range(column):
                (
                    matrix[row_index][column_index],
                    matrix[row - row_index - 1][column_index],
                ) = (
                    matrix[row - row_index - 1][column_index],
                    matrix[row_index][column_index],
                )

    def flip_diagonal(self, matrix):
        row = column = len(matrix)
        for row_index in range(row):
            for column_index in range(row_index):
                matrix[row_index][column_index], matrix[column_index][row_index] = (
                    matrix[column_index][row_index],
                    matrix[row_index][column_index],
                )

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.turn_up_side_down(matrix)
        self.flip_diagonal(matrix)
