class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n & 1 # right most bit
            res = (res << 1) | bit
            n = n >> 1
        return res  