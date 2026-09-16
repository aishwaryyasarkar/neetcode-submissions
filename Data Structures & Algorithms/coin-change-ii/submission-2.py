class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = {}
        def dfs(i, amt):
            if amt == amount:
                return 1
                
            if i >= len(coins):
                return 0

            if amt > amount:
                return 0

            if (i, amt) in mem:
                return mem[(i, amt)]

            # include current
            include = dfs(i, amt+coins[i])

            # skip
            skip = dfs(i+1, amt)

            mem[(i, amt)] = include + skip

            return include + skip

        return dfs(0, 0)