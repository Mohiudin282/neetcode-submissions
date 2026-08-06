class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        l = 0
        r = l + 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxi = max(maxi, profit)
            if profit < 0:
                l=r
                r+=1
            else:
                r+=1
        return maxi
            