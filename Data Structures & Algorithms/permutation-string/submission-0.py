class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Trick: 
        1. create 2 arrays of 26, and increment by 1 based on s1 and s2
        2. have a window of l->r same length of s1, and slide it on s2
        3. have a matches counter, initially match is 0
        4. generate current match between s1 and s2 // there should be a way here to detect if there is something is s1 that is not in s2
        5. if match == 26, return True
        6. every new char on the right means increment in s2 hashmap
            a. if incrementing s2 hash, now gives a match, increase match
            b. elseif if it was already a match, and we made it too large (+1), so s2[idx]-s1[idx]=1
        7. index of l, to be removed
        8. every char removed on the left means decrement in s2 hashmap
            a. if by decreasing we led to a match, increase match
            b. if this led to removing a match (i.e., val reduced by 1), s1[idx]-s2[idx]=1 decrease match 
        9. increase l by 1 (since it is a window, and we have increased r)
        return match == 26

        Remember: match is between s1 and a slice of s2 (not whole s2)
        s1: abc
        s2: xabc

        s1_map = [a:1, b:1, c:1, ...]
        s2_map = [x:1, a:1, b:1, ...]
        
        """

        # edge case
        if len(s1) > len(s2): return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] +=1
            s2_count[ord(s2[i]) - ord('a')] +=1
            
        matches = 0

        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches+=1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2_count[index]+=1

            if s2_count[index] == s1_count[index]:
                matches+=1
            elif s2_count[index] - s1_count[index] == 1:
                matches-=1

            # focused on what is removed from window
            index = ord(s2[l]) - ord('a')
            s2_count[index]-=1
            if s2_count[index] == s1_count[index]:
                matches+=1
            elif s1_count[index] - s2_count[index] == 1:
                matches-=1

            l+=1
            
        return matches == 26


        

