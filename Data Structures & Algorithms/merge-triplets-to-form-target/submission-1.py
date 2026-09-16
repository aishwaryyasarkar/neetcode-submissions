class Solution:
    """
    for every col, find max and see if it matches with the the same idx in target
    """
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        cols = len(triplets[0])

        for t in triplets:
            # discard invalid triplets
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i in range(cols):
                if t[i] == target[i]:
                    found[i] = True
                
        return all(found)
