class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two = 0

        for i in reversed(range(len(cost))):
            one = cost[i]
            cost[i-1] = min(cost[i-1]+one, cost[i-1]+two)
            temp = one
            one = cost[i-1]
            two = temp

        return min(cost[0],cost[1])

            