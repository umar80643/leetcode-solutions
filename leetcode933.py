class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        while self.counter[0] < t - 30000:
            self.counter.pop(0)
        return len(self.counter)


recentCounter = RecentCounter();
recentCounter.ping(1);
recentCounter.ping(100);
recentCounter.ping(3001);
recentCounter.ping(3002);

