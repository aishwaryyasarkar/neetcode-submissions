class Solution:
    """
    Note: always positive
    1, 1+2, 1+3, 1+4, 1+2+3, 1+2+4 .. 4
    2+1, 2+3, 2+4... 1
    3+1, 3+2, 3+1+4, 3+2+4
    """
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        mem = {}

        def backtrack(i, sumNum):
            if sumNum == target:
                return True

            if i == len(nums):
                return False 

            if (i,sumNum) in mem:
                return mem[(i, sumNum)]

            # take curr
            sumNum += nums[i]
            res1 = backtrack(i+1, sumNum)
            mem[(i, sumNum)] = res1

            # skip curr
            sumNum -= nums[i]
            res2 = backtrack(i+1, sumNum)

            

            return res1 or res2

        return backtrack(0, 0)
