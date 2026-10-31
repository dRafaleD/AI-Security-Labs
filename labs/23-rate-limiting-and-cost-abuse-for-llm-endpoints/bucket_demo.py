"""Token-bucket rate limiter with request cost, driven by a fake clock."""


class Bucket:
    def __init__(self, capacity=5, refill_per_s=1.0):
        self.capacity, self.refill, self.tokens, self.last = capacity, refill_per_s, capacity, 0.0

    def allow(self, now, cost=1):
        self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.refill)
        self.last = now
        if cost > self.tokens:
            return False
        self.tokens -= cost
        return True


if __name__ == "__main__":
    b = Bucket()
    burst = [b.allow(0.0) for _ in range(10)]
    print("burst  :", burst)
    later = b.allow(3.0)
    print("after 3s:", later)
    huge = Bucket().allow(0.0, cost=50)
    print("huge prompt:", huge)
    assert burst.count(True) == 5 and burst.count(False) == 5
    assert later is True
    assert huge is False
    print("PASS: bursts are capped, tokens refill over time and costly requests are rejected.")
    print("Review: rate limiting reduces abuse and cost, not injection or leakage.")
