class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjList = {}
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if pattern not in adjList:
                    adjList[pattern] = []
                adjList[pattern].append(word)

        q = deque()
        visited = set()
        visited.add(beginWord)
        q.append(beginWord)
        count = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in adjList[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)

            count+=1

        return 0

