class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy_idx=0
        sell_idx=0
        profit = set()

        if len(prices)<2:
            return 0

        if prices[0]>prices[1]:
            buy=prices[1]
            buy_idx=1
        else:
            buy=prices[0]
            buy_idx=0
            sell=prices[1]
            sell_idx=1
        
        prof = sell - buy
        if prof>0:
            profit.add(prof)

        for i in range(2, len(prices)):
            if buy>prices[i]:
                buy=prices[i]
                buy_idx=i
                sell=0
                sell_idx=0

            if buy < prices[i] and buy_idx < i and prices[i]>sell:
                sell = prices[i]
                sell_idx=i

            prof = sell - buy
            if prof>0:
                profit.add(prof)

        print(profit)
        return max(profit, default=0)

            

