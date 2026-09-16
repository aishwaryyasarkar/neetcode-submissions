
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(i, curr):
            if i == len(word):
                return curr.endOfWord

            if word[i] not in curr.children and word[i] != ".":
                return False
            
            if word[i] == ".":
                for c in curr.children:
                    if dfs(i+1, curr.children[c]):
                        return True
                return False

            return dfs(i + 1, curr.children[word[i]])

        return dfs(0, curr)
                
