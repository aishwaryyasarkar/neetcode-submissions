class Solution:
    """
    for every col, find max and see if it matches with the the same idx in target
    """
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        hasTarget = [False, False, False]

        # filter unsafe triplets
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            if t[0] == target[0]:
                hasTarget[0] = True
            
            if t[1] == target[1]:
                hasTarget[1] = True

            if t[2] == target[2]:
                hasTarget[2] = True

        return all(hasTarget)
            
            

        