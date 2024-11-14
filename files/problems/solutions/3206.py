class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colour_len = len(colors)
        if colour_len < 2:
            return 0
        window = "".join(map(str, colors[:3]))
        total_patterns = 0
        for i in range(colour_len):
            window = window[1:] + str(colors[(i + 3) % colour_len])
            if window == "101" or window == "010":
                total_patterns += 1
        return total_patterns
