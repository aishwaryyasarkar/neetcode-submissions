class Solution:
    """
    Input: nums = [1,2,1,0,4,2,6], k = 3
    Output: [2,2,4,4,6]
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        q = deque()
        res = []
        
        if not nums:
            return []

        while right <= len(nums) - 1:
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)
            
            if (right - left + 1) == k:
                res.append(nums[q[0]])
                left+=1
                if q[0] < left:
                    q.popleft()
            right+=1
            
        return res