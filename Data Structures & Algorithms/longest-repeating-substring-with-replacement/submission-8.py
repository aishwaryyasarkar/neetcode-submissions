class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_length = len(s)
        left, right = 0, 0
        max_l = 0
        freq = {}

        while right <= s_length - 1:
            if s[right] not in freq:
                freq[s[right]]=1

            w_length = (right - left) + 1
            print(w_length, s[right], freq, max(freq.values()), max_l)
            # valid subs
            if w_length -  max(freq.values()) <= k:
                print("increased right from ", right, right+1)
                
                right+=1

                if right <= s_length - 1:
                    # new right not present
                    if s[right] not in freq:
                        freq[s[right]]=1
                    else:
                        freq[s[right]]+=1

                if w_length > max_l:
                    max_l = w_length
            else:
                print("increased left from ", left, left+1)
                freq[s[left]]-=1
                left+=1
        
        return max_l