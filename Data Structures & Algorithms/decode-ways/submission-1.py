class Solution:
    def numDecodings(self, s: str) -> int:
        comboList = [-1] * len(s)

        def combo(i):
            # when i has not reached the end but encountered a 0, break and return
            if i <= len(s) - 1 and s[i] == "0":
                return 0

            # when i has reached the end, break
            if i >= len(s):
                return 1
            
            if comboList[i] != -1:
                return comboList[i]

            count = 0

            # just me
            count += combo(i+1) # 0

            # me and my neighbor, 2 digit branch range is 10->26
            if 10 <= int(s[i:i+2]) <= 26:
                count += combo(i+2)

            comboList[i] = count

            return count

        return combo(0)