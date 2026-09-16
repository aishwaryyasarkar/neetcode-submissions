class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set
        myset = set(nums)
        sequence_length=[]
        print(myset)
        max_count=0
        count=0
        for n in myset:
            if n-1 not in myset:
                start=n
                count+=1
                while True:
                    print(count, start)
                    if start+1 in myset:
                        count+=1
                        start+=1
                    else:
                        break
            else:
                continue

            if count > max_count:
                max_count=count
            count=0

        return max_count


