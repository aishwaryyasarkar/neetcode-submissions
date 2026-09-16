class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s = "YOXAZV"
        t = "XYZ"
        t_count = X:1, Y:1, Z:1
        s_count = Y:1, O:1, X:1, A:1, Z:1, V:1
        """
        from collections import defaultdict

        l, r = 0, 0
        need = {}
        curr_window = {}
        res = ""
        min_s = float('inf')

        for char in t:
            if char not in need:
                need[char] = 1
            else:
                need[char] += 1
        required = len(need)
        print(need)

        while l<=r:
            
            # is it a match?
            if required > 0:
                if r >= len(s):
                    break
                # add curr r char to count
                if s[r] not in curr_window:
                    curr_window[s[r]]=1
                else:
                    curr_window[s[r]]+=1
                    
                if s[r] in need and curr_window[s[r]]==need[s[r]]:
                    required-=1
                r+=1
            
            if required == 0 and l < r:
                if (r-l) < min_s:
                    min_s = r-l
                    res = s[l:r]

                curr_window[s[l]]-=1

                if s[l] in need and need[s[l]]-curr_window[s[l]]==1:
                    required+=1               
                l+=1
        return res

        
                

