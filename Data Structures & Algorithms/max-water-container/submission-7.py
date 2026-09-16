class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container = 0
        left, right = 0, len(heights)-1
        while left < right:
            container = max(container, min(heights[left], heights[right]) * (right-left))
            # print(left,right, container)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1


        return container

