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
        words = set(wordDict)
        maxLen = max(map(len, wordDict))
        memo = {}

        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for j in range(i + 1, min(len(s), i + maxLen) + 1):
                if s[i:j] in words and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)