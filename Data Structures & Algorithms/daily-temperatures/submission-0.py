class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = len(temperatures) * [0]
        stack = deque()

        for idx, t in enumerate(temperatures):
            if not stack:
                stack.append((t, idx))

            while stack and stack[-1][0]<t:
                t_s, idx_s = stack.pop()
                res[idx_s] = idx - idx_s

            stack.append((t, idx))

        return res

