class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinMem = {}

        def dfs(i, localAmount):
            if i >= len(coins):
                return float('inf')

            if localAmount > amount:
                return float('inf')
            
            if localAmount == amount:
                return 0

            count1, count2 = 0, 0

            if (i,localAmount) in coinMem:
                return coinMem[(i, localAmount)]
            
            # include i
            count1 = 1 + dfs(i, localAmount + coins[i])

            # exclude i
            count2 = dfs(i+1, localAmount)

            coinMem[(i, localAmount)] = min(count1, count2)

            return min(count1, count2)

        res = dfs(0, 0)

        if res == float('inf'):
            return -1

        return res