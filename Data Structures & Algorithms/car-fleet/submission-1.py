class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        target = 10, position = [1,4], speed = [3,2]
        1. sort pos desc to know which car is ahead of it
        """

        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort(reverse=True)

        stack = []
        stack.append(pos_speed[0])

        """
        [(7, 1), (4, 2), (1, 2), (0, 1)]
        stack = [ (7,1) (1,2) 10-1/2=4 ] (0,1), 10-0/1=10
        """

        for i in range(1,len(pos_speed)):
            curr_pos, curr_speed = pos_speed[i]
            pos, speed = stack[-1]

            if ((target-curr_pos)/curr_speed) > ((target-pos)/speed):
                stack.append((curr_pos, curr_speed))
        
        return len(stack)

        

