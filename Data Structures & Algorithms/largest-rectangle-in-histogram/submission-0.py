class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        """
        [7,1,7,2,2]
        start = 3, 2
        maxArea = 7 * 1 = 7, 7 * (3-2)
        idx, height = 2, 7
        stack = [(1,1), (3, 2)] 
        """
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea