class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            oneWay = cost[i] + cost[i+1]
            twoWay = cost[i] + cost[i+2]
            cost[i] = min(oneWay, twoWay)

        return min(cost[0], cost[1])