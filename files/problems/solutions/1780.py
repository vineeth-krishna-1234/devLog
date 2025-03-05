class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        powers = []
        for power in range(16, -1, -1):
            if not n:
                break
            current_power_value = pow(3, power)
            if current_power_value <= n:
                powers.append(power)
                n = n - current_power_value

        return not n and len(powers) == len(set(powers))
