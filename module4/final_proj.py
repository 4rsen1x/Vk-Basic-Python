from typing import List

class Twitter:
    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.time = 0

    def post_tweet(self, user_id, tweet_id):
        if user_id not in self.tweets:
            self.tweets[user_id] = []
        self.time += 1
        self.tweets[user_id].append((self.time, tweet_id))

    def get_news_feed(self, user_id) -> List[int]:
        news_feed = []
        following = self.followers.get(user_id, set()) | {user_id}
        for user in following:
            if user in self.tweets:
                news_feed.extend(self.tweets[user])
        news_feed.sort(reverse=True, key=lambda x: x[0])
        return [tweet_id for _, tweet_id in news_feed[:10]]

    def follow(self, follower_id, followee_id):
        if follower_id not in self.followers:
            self.followers[follower_id] = set()
        self.followers[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        if follower_id in self.followers:
            self.followers[follower_id].discard(followee_id)
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
 
