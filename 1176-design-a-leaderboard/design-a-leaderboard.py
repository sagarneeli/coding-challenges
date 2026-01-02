class Leaderboard:

    def __init__(self):
        self.heap = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.heap:
            self.heap[playerId] += score
        else:
            self.heap[playerId] = score

    def top(self, K: int) -> int:
        scores = self.heap.values()
        top_K = sorted(scores, reverse=True)[:K]
        return sum(top_K)

    def reset(self, playerId: int) -> None:
        del self.heap[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)