class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        grid_len = len(grid)

        hash_table = {key: 0 for key in range(1, (grid_len**2) + 1)}

        for x_index in range(grid_len):
            for y_index in range(grid_len):
                element_at_index = grid[x_index][y_index]
                hash_table[element_at_index] = hash_table[element_at_index] + 1

        return_value = [0, 0]
        for key, count in hash_table.items():
            if count == 2:
                return_value[0] = key
            if not count:
                return_value[1] = key
        return return_value
