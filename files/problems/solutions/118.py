class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pascal_triangle = []
        for row in range(1, numRows + 1):
            current_row = []
            for index in range(row):
                if index == 0 or index == row - 1:
                    current_row.append(1)
                else:
                    current_row.append(
                        pascal_triangle[row - 2][index - 1]
                        + pascal_triangle[row - 2][index]
                    )
            pascal_triangle.append(current_row)
        return pascal_triangle
