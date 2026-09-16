class Solution:
    """
    1. start iterating dict to find first letter match with s
    2. keep iterating characters in s and that element of dict until the end of the match, till it breaks O(len(dict)+O(len(dict[elem])))
    3. When it breaks, the char that was a mismatch becomes the query for next search

    alternative:
    1. iterate through dict once and use a hashmap to store starting letter of each element and its idx in the dict
    n: 0
    c: 1
    // O(len(dict)) // dict can have duplicate / common forst letters, then append idx
    
    2. Iterate through word, and look at hashmap to get idx for matching.. break when mismatch
    3. start with first mismatch again.. if it is not found in hashmap, return False


    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.firstMap = {}
        self.wordDict = wordDict
        self.s = s
        self.memo = {}

        for idx, word in enumerate(self.wordDict):
            firstLetter = word[0]
            if firstLetter not in self.firstMap:
                self.firstMap[firstLetter] = []
            self.firstMap[firstLetter].append(idx)

        print(self.firstMap)

        return self.findMismatch(0)
        
    def findMismatch(self, charidx):
        start = self.s[charidx]
        
        if charidx in self.memo:
            return self.memo[charidx]

        if start not in self.firstMap:
            self.memo[charidx] = False
            return False

        for i in self.firstMap[start]:
            refWord = self.wordDict[i]
            refWordidx = 0
            sidx = charidx

            while refWordidx <= len(refWord) - 1 and sidx <= len(self.s) - 1 and refWord[refWordidx] == self.s[sidx]:
                refWordidx += 1
                sidx += 1

            if refWordidx == len(refWord):
                if sidx == len(self.s) or self.findMismatch(sidx): # char in word of dict exhausted, but char in string is not
                    self.memo[charidx] = True
                    return True
            
            continue
        self.memo[charidx] = False
        return False







        
