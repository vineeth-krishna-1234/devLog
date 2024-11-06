class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        prev_altitude =0
        max_altitude = 0
        for value in gain:
            current_gain = prev_altitude + value
            max_altitude = max(current_gain,max_altitude)
            prev_altitude = current_gain
        return max_altitude