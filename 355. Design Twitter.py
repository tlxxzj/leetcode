class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict, namedtuple
        self.Tweet = namedtuple('Tweet', ['userId', 'tweetId'])
        self.followees = defaultdict(set)
        self.tweets = []


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.append(self.Tweet(userId=userId, tweetId=tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news = []
        followees = self.followees[userId]
        for i in range(len(self.tweets)-1, -1, -1):
            tweet = self.tweets[i]
            if (tweet.userId == userId) or (tweet.userId in followees):
                news.append(tweet.tweetId)
                if len(news) == 10:
                    break
        return news


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)