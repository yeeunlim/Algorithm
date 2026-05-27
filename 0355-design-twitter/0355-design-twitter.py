import heapq
from typing import List

# Tweet 클래스: 트윗 데이터 캡슐화
class Tweet:
    def __init__(self, tweet_id: int, timestamp: int):
        self.id = tweet_id
        # 최신 트윗을 Min-Heap에서 우선순위로 뽑기 위해 시간값을 음수로 저장
        self.time = timestamp 

# User 클래스: 유저의 상태(팔로우, 트윗)와 행동 정의
class User:
    def __init__(self, user_id: int):
        self.id = user_id
        # 본인의 트윗도 뉴스 피드에 포함되어야 하므로, set 생성 시 자기 자신을 팔로우하도록 초기화
        self.following = {user_id} 
        self.tweets = [] # 자신이 작성한 Tweet 객체들이 시간순으로 쌓이는 리스트

    def follow(self, followee_id: int) -> None:
        """다른 유저를 팔로우합니다."""
        self.following.add(followee_id)

    def unfollow(self, followee_id: int) -> None:
        """다른 유저를 언팔로우합니다. (단, 자기 자신은 언팔로우할 수 없습니다.)"""
        if followee_id != self.id and followee_id in self.following:
            self.following.remove(followee_id)

    def post_tweet(self, tweet_id: int, timestamp: int) -> None:
        """새로운 트윗을 작성하여 본인의 트윗 리스트에 추가합니다."""
        self.tweets.append(Tweet(tweet_id, timestamp))

# 메인 시스템 클래스: 유저 객체를 관리하고 흐름을 제어
class Twitter:
    def __init__(self):
        # 유저 ID를 User 객체에 매핑합니다.
        self._users = {} 
        # 전역 시간 카운터: 시간이 지날수록 감소(-1, -2...)하여 Min-Heap에서 가장 먼저 추출되도록 합니다.
        self._timestamp = 0 

    def _get_user(self, user_id: int) -> User:
        """유저가 존재하지 않으면 새로 생성하여 반환하는 헬퍼 메서드입니다."""
        if user_id not in self._users:
            self._users[user_id] = User(user_id)
        return self._users[user_id]

    def postTweet(self, userId: int, tweetId: int) -> None:
        """새로운 트윗을 등록합니다."""
        user = self._get_user(userId)
        user.post_tweet(tweetId, self._timestamp)
        self._timestamp -= 1 # 다음 트윗은 더 작은 음수 값을 가지게 됩니다.

    def getNewsFeed(self, userId: int) -> List[int]:
        """나와 팔로우한 사람들의 가장 최신 트윗 10개를 반환합니다."""
        if userId not in self._users:
            return []

        user = self._get_user(userId)
        news_feed = []
        heap = []

        # 힙 초기화: 각 유저의 가장 최신 트윗(리스트의 마지막 원소)을 힙에 삽입
        for target_id in user.following:
            if target_id in self._users:
                target_user = self._users[target_id]
                if target_user.tweets:
                    last_idx = len(target_user.tweets) - 1
                    tweet = target_user.tweets[last_idx]
                    
                    # 힙 저장 구조: (시간(음수), 트윗ID, 다음 트윗 인덱스, 해당 유저의 트윗 리스트)
                    heapq.heappush(
                        heap, 
                        (tweet.time, tweet.id, last_idx - 1, target_user.tweets)
                    )

        # K-way Merge: 힙에서 최대 10개의 최신 트윗을 추출
        while heap and len(news_feed) < 10:
            time, tweet_id, next_idx, tweets_list = heapq.heappop(heap)
            news_feed.append(tweet_id)

            # 추출한 트윗 유저의 다음으로 최근인 트윗이 있다면 힙에 보충
            if next_idx >= 0:
                next_tweet = tweets_list[next_idx]
                heapq.heappush(
                    heap, 
                    (next_tweet.time, next_tweet.id, next_idx - 1, tweets_list)
                )

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """follower가 followee를 팔로우하도록 시스템에 요청합니다."""
        follower = self._get_user(followerId)
        self._get_user(followeeId) # followee가 시스템에 없을 수 있으므로 생성 보장
        follower.follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """follower가 followee를 언팔로우하도록 시스템에 요청합니다."""
        follower = self._get_user(followerId)
        follower.unfollow(followeeId)