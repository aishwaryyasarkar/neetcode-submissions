class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.TweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # list of tweets ordered from most recent up to 10
        minHeap = []
        self.followMap[userId].add(userId)
        follows = self.followMap[userId]

        for followee_Id in follows:
            if followee_Id in self.TweetMap:
                index = len(self.TweetMap[followee_Id]) - 1
                count, tweetId = self.TweetMap[followee_Id][index]
                minHeap.append([count, tweetId, followee_Id, index - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followee_Id, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            if index >= 0:
                count, tweetId = self.TweetMap[followee_Id][index]
                heapq.heappush(minHeap, [count, tweetId, followee_Id, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
