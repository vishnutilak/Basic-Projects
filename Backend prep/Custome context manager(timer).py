import time
class timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.end = time.perf_counter()
        print(f"Elapsed: {self.end - self.start:.6f}s")

# usage:
# with timer():
#    do_work()
