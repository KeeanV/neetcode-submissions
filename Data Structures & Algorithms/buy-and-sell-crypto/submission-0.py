class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(len(prices)):
            curr_profit = prices[right] - prices[left]
            max_profit = max(curr_profit, max_profit)
            if prices[left] > prices[right]:
                left = right
        return max_profit