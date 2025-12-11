from threading import Lock

class ThreadSafeCounter:
    def __init__(self):
        self._val = 0
        self._lock = Lock()

    def inc(self, delta=1):
        with self._lock:
            self._val += delta
            return self._val

    def get(self):
        with self._lock:
            return self._val
