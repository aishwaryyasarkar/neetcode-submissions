class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        nums1 = [1,2]
        nums2 = [3]

        """

        total_length = len(nums1) + len(nums2)
        left = total_length // 2

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        start, end = -1, len(nums2) - 1
        while start <= end:
            mid2 = (start+end) // 2
            mid1 = left - (mid2+1) - 1

            left1  = nums1[mid1] if mid1 >= 0 else float("-inf")
            right1 = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float("inf")

            left2  = nums2[mid2] if mid2 >= 0 else float("-inf")
            right2 = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float("inf")

            if left1 <= right2 and left2 <= right1:
                if total_length % 2 == 0:
                    median = (min(right1, right2) + max(left1, left2)) / 2
                else:
                    median = min(right1, right2)
                return median
            elif left1 > right2:
                start = mid2+1
            elif left2 > right1:
                end = mid2-1
        