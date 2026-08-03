from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        # tweets[user] = [(time, tweetId), ...]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1        # smaller value = newer tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:
            if self.tweets[followee]:
                idx = len(self.tweets[followee]) - 1
                time, tweet = self.tweets[followee][idx]
                heapq.heappush(heap, (time, tweet, followee, idx - 1))

        res = []

        while heap and len(res) < 10:
            time, tweet, followee, idx = heapq.heappop(heap)
            res.append(tweet)

            if idx >= 0:
                time, tweet = self.tweets[followee][idx]
                heapq.heappush(heap, (time, tweet, followee, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)