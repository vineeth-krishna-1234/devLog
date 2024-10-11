class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_value = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - min_value

            max_profit = max(max_profit,profit)
            if price< min_value:
                min_value = price
        return max_profit