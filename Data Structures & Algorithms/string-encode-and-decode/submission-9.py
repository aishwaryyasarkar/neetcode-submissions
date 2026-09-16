class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        count = len(strs)
        sub_list = []
        for s in strs:
            l = len(s)
            sub_list.append(l)
            sub_list.append('#')
            for c in s:
                sub_list.append(c)
        s = "".join(str(item) for item in sub_list)
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        if len(s)==0:
            return []
        output = []
        scan_head=0
        end = scan_head
        while s[end] != '#':
            end += 1
        l_of_substring = int(s[scan_head:end])
        scan_head = end + 1 
        while scan_head <= len(s):
            word = ""
            for idx in range(int(l_of_substring)):
                # if(s[scan_head] != "#"):
                word+="".join(s[scan_head])
                scan_head+=1
            output.append(word)
            if scan_head >= len(s):
                break
            end = scan_head
            while s[end] != '#':
                end += 1
            l_of_substring = int(s[scan_head:end])
            scan_head = end + 1
        print(output)
        return output



