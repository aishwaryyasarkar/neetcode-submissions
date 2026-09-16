class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [3,4,5,6], target = 9, o/p= [0,1]
        hashmap = {3:0, 4:1}

        loop through the arr
            check if target - nums[i] is visited
                idx_s =hashmap[target - i]
                return [idx_s,i
            keep adding to hashmap
        """
        visited = {}
        for i in range(len(nums)):
            if target - nums[i] in visited:
                idx = visited[target - nums[i]]
                return [idx,i]
            visited[nums[i]]=i
        
        return []
