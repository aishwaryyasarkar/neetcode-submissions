class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1   2   4  8
        10 11  12  13
        14 20  30  40

        """

        # binary search to find row
        # if target is between r_i and r_j, it may be a member of r_j
        # so r-l = 1, then it is part of r
        l, r = 0, len(matrix)-1
        candidate_row = -1
        """
            target = 101
                    m,   c
            7 20 60 100 300
                         l,r
        """

        # binary search to find col
        l, r = 0, (len(matrix)*len(matrix[0])-1)

        """
           m=1
        10 11 12 13
        l,r         r
        """
        while l<=r:
            mid = (l+r)//2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] > target:
                r=mid-1
            elif matrix[row][col] < target:
                l=mid+1
            else:
                return True
        
        return False
        



