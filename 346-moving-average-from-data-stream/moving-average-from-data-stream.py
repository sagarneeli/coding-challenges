class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.nums = deque()

    def next(self, val: int) -> float:
        if len(self.nums) == self.size:
            self.nums.popleft()
        self.nums.append(val)
        return sum(self.nums) / len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)