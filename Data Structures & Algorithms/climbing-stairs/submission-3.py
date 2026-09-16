class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one


        # recursion
        # if n < 1:
        #     return 0

        # def recursion(i):
        #     # base cases
        #     if i > n:
        #         return 0

        #     if i == n:
        #         return 1

        #     return recursion(i+1) + recursion(i+2)

            
        # return recursion(0)
        