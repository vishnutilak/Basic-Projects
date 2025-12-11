import time
from functools import wraps
from collections import deque

class RateLimitExceededError(Exception):
    """Custom exception raised when the rate limit is exceeded."""
    pass

# Dictionary to store call timestamps for each function/key
# Structure: {('function_name', 'key'): deque([timestamp1, timestamp2, ...]), ...}
_CALL_HISTORY = {}

def rate_limit(limit, period):
    def decorator(func):
        # Unique identifier for the function (used in the global history)
        func_id = func.__name__

        @wraps(func)
        def wrapper(key, *args, **kwargs):
            # Combine function ID and user-specific key (e.g., user ID or IP)
            unique_key = (func_id, key)
            
            # Initialize history for this key if it doesn't exist
            if unique_key not in _CALL_HISTORY:
                _CALL_HISTORY[unique_key] = deque()
            
            history = _CALL_HISTORY[unique_key]
            now = time.time()
            
            # 1. Clean up old timestamps (outside the period)
            # Remove timestamps that are older than the defined period
            while history and history[0] < now - period:
                history.popleft()
                
            # 2. Check the limit
            if len(history) >= limit:
                # Limit exceeded: raise the custom exception
                raise RateLimitExceededError(
                    f"Rate limit exceeded for key '{key}'. Max {limit} calls every {period} seconds."
                )
            
            # 3. Add the new timestamp and execute the function
            history.append(now)
            return func(key, *args, **kwargs)
        
        return wrapper
    return decorator
