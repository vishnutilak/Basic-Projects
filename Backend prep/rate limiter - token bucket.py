import time
from threading import Lock

class TokenBucket:
    def __init__(self, capacity, refill_rate_per_sec):
        self.capacity = capacity
        self.tokens = capacity
        self.rate = refill_rate_per_sec
        self.last = time.monotonic()
        self.lock = Lock()

    def allow(self, tokens=1):
        with self.lock:
            now = time.monotonic()
            delta = now - self.last
            self.last = now
            self.tokens = min(self.capacity, self.tokens + delta * self.rate)
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

# usage per user:
buckets = {}  # user_id -> TokenBucket
def allow_request(user_id):
    if user_id not in buckets:
        buckets[user_id] = TokenBucket(capacity=100, refill_rate_per_sec=100/60.0)
    return buckets[user_id].allow()
