class Solution:
    """
    1. start iterating and choosing subsequence
    2. start becomes a candidate
    3. only increase length if an element is > than candidate, and when that happens, this element becomes the candidate
    4. continue till the end and record length
    5. increase start by 1
    // O(n^2)


    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLength = 0
        self.mem = {}
        
        def findLength(cidx, curr):
            if curr == len(nums):
                return 1

            length = 0
            while curr <= len(nums) - 1:
                if nums[curr] > nums[cidx]:
                    if curr in self.mem:
                        currLength = self.mem[curr] # find in cache the subsequence length if already precomputed
                    else:
                        currLength = findLength(curr, curr+1)
                        if curr not in self.mem:
                            self.mem[curr] = 0
                            self.mem[curr] = currLength
                    length = max(length, currLength) # this is req because we are returning length multiple time in the while loop, we need to finally return the max length from this curr
                curr+=1


            return length+1

        for i in range(len(nums)):
            if i+1 <= len(nums):
                length = findLength(i, i+1)
                print(length)
                maxLength = max(maxLength, length)
        return maxLength