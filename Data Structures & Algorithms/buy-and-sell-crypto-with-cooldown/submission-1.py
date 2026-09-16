class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown = 2
        mem = {}

        def dfs(i, state):
            if i >= len(prices):
                return 0

            profit = 0

            if (i,state) in mem:
                return mem[(i,state)]

            if not state: # sold already
                # buy today
                state = True # change to bought
                buyProfit = -prices[i] + dfs(i+1, state)

                # skip today
                state = False
                skipProfit = dfs(i+1, state) 

                mem[(i,state)] = max(buyProfit, skipProfit)
                return max(buyProfit, skipProfit)

            else:
                # sell today
                state = False # sold
                sellProfit = prices[i] + dfs(i+cooldown, state)

                # skip today
                state = True
                skipProfit = dfs(i+1, state) 

                mem[(i,state)] = max(sellProfit, skipProfit)

                return max(sellProfit, skipProfit)
            
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, dfs(i, False))

        return maxProfit