class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(len(prices)-1):
            buy=prices[i]
            profit=0
            for j in range(i+1,len(prices)):
                if prices[j]>buy:
                    profit=prices[j]-buy
                    max_profit=max(profit,max_profit)
        return max_profit