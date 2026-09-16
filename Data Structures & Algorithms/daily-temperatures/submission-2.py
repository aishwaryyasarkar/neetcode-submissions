class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        temperatures = [30,38,30,36,35,40,28]
        
        stack = [(40,i)] 28
        res = [1,4,1, 2, 1, 0, 0]  
        """

        stack = []
        res = [0] * len(temperatures)

        for curr_i, curr_t in enumerate(temperatures):
            if stack:
                while stack:
                    temp, idx = stack[-1]
                    if curr_t > temp:
                        stack.pop()
                        res[idx]=curr_i-idx
                    else:
                        break
            stack.append((curr_t,curr_i))

        return res
            
