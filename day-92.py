#Function caching
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fibonacci(n : int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return 0
    return fibonacci(n - 1)+fibonacci(n - 2)

start = time.perf_counter()
print(fibonacci(35))  # 35 is enough to notice delay
end = time.perf_counter()
print(f"Execution time (no cache): {(end - start) * 1000} ms")
