import collections
import heapq

class Twitter:

    def __init__(self):
        # 트윗의 최신 순서를 결정하기 위한 시간 변수 (음수로 사용하여 Min-Heap을 Max-Heap처럼 활용)
        self.time = 0
        # 유저별 작성한 트윗 리스트: {userId: [(time, tweetId)]}
        self.tweets = collections.defaultdict(list)
        # 유저별 팔로우 목록: {userId: set(followeeIds)}
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """새로운 트윗을 작성합니다."""
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1 # 시간이 지날수록 작은 값을 가지도록 하여 우선순위를 높임

    def getNewsFeed(self, userId: int) -> list[int]:
        """본인과 팔로우한 사람들의 가장 최근 트윗 10개를 가져옵니다."""
        res = []
        heap = []
        
        # 피드를 구성할 대상 유저 집합 (본인 포함)
        users = self.followees[userId] | {userId}
        
        # 각 유저의 가장 최근 트윗(리스트의 마지막 원소)을 힙에 삽입
        for u in users:
            if self.tweets[u]:
                index = len(self.tweets[u]) - 1
                tweet_time, tweetId = self.tweets[u][index]
                # 힙에 저장할 데이터: (시간, 트윗ID, 작성자ID, 다음 트윗 인덱스)
                heapq.heappush(heap, (tweet_time, tweetId, u, index - 1))
        
        # 힙에서 최대 10개의 최신 트윗을 추출
        while heap and len(res) < 10:
            tweet_time, tweetId, u, index = heapq.heappop(heap)
            res.append(tweetId)
            
            # 해당 유저의 다음으로 최근인 트윗이 존재한다면 힙에 추가
            if index >= 0:
                next_time, next_id = self.tweets[u][index]
                heapq.heappush(heap, (next_time, next_id, u, index - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """follower가 followee를 팔로우합니다."""
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """follower가 followee를 언팔로우합니다."""
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
