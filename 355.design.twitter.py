class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []
        self.follows = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets.append((userId, tweetId))
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        ret = []
        follow = self._getfollows(userId)
        for t in self.tweets[::-1]:
            if t[0] == userId or t[0] in follow:
                ret.append(t[1])
                if len(ret) == 10: break
        return ret
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self._getfollows(followerId).add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self._getfollows(followerId):
            self._getfollows(followerId).remove(followeeId)
    
    def _getfollows(self, id):
        if self.follows.get(id, None) is None:
            self.follows[id] = set()
        return self.follows[id]
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)