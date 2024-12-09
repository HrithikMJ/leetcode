# 2ptr
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 ptr
        # if
        b, s = 0, 1
        maxVal = 0
        while s < len(prices):
            if prices[b] < prices[s]:
                maxVal = max(maxVal, prices[s] - prices[b])
            else:
                b = s
            s = s + 1
        return maxVal
