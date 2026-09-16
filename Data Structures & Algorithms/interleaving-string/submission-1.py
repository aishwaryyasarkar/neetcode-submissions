class Solution:
    """
    iterate through s3.. and see which of s1 and s2 is the starting string..
    compare characters one by one.. and break when mismatch
    after comparing with s1, compare with s2..
    you cannot have s1, s1 or s2, s2.. they should be alternating and each time there must be a match
    also, cannot keep greedily choosing from s1 / s2, if a character is equal in both s1 and s2, consider taking from either
    index of s3 will be i + j
    

    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        mem = {}

        if len(s1) + len(s2) != len(s3):
            return False
        
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in mem:
                return mem[(i, j)]
            
            k = i + j
            res_s1, res_s2 = False, False

            # check in s1
            if i < len(s1) and s1[i] == s3[k]:
                res_s1 = dfs(i+1, j)

            # check in s2
            if j < len(s2) and s2[j] == s3[k]:
                res_s2 = dfs(i, j+1)

            mem[(i, j)] = res_s1 or res_s2

            return res_s1 or res_s2

        
        return dfs(0, 0)

        