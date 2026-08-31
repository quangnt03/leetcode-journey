class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        p_min = prices[0]
        for i in range(1, len(prices)):
            result = max(prices[i] - p_min, result)
            p_min = min(prices[i], p_min)
        return result