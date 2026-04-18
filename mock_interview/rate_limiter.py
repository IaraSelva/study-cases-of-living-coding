# Implement a per-user rate limiter
# Each user may issue at most 3 requests in any rolling 10-second window.
# Design a Python class:

# class RateLimiter:
#     def allow_request(self, user_id: str) -> bool:
#         """Return True if the request *should be allowed* right now, else False."""
# Use time.time() (seconds since epoch) for timestamps.
# Optimise for O(1) average-time per call and reasonable memory.
# Think aloud about edge-cases (bursts, first request, long-idle users).
# Follow-ups we may cover if time allows
# Thread-safety: what locks or data structures would you add?
# Distributed system: how would you keep limits consistent across servers (Redis, token bucket, etc.)?

from collections import deque
import datetime
import time

class RateLimiter:
    def __init__(self, time_limit: int = 10, call_limit: int = 3):
        self.users = {} # dict of user_id: deque of timestamps 
        self.time_limit = datetime.timedelta(seconds=time_limit)
        self.call_limit = call_limit

    def allow_request(self, user_id):
        print(f"user = {user_id}")
        curr_call_timestamp = datetime.datetime.now()
        # check if the user exists
        # add the timestamp of the call into deque and dict
        # if yes, check the timestamp of the older call
        # pop all the requests older than time limit
        # check if the size of the deque is still greater than call limit
        # if it is, return False otherwise true
        self.set_user_timestamp(curr_call_timestamp, user_id)

        calls_amount = self.check_last_calls(curr_call_timestamp, user_id)

        if calls_amount > self.call_limit:
            return False    
        return True
    
    def check_last_calls(self, curr_call_timestamp, user_id):
        last_calls_timestamp = self.get_user_timestamp(user_id)
        print(f"time diff {curr_call_timestamp - last_calls_timestamp[0]}")
        while last_calls_timestamp and curr_call_timestamp - last_calls_timestamp[0] >= self.time_limit:
            print(f"last_calls = {last_calls_timestamp}")
            last_calls_timestamp.popleft()
        
        return len(last_calls_timestamp)

    def get_user_timestamp(self, user_id):
        return self.users.get(user_id)
    
    def set_user_timestamp(self, curr_call_timestamp, user_id):
        timestamp_record = self.users.get(user_id)
        if not timestamp_record:
            timestamp_record = deque()
        timestamp_record.append(curr_call_timestamp)
        self.users[user_id] = timestamp_record

rate_limiter = RateLimiter()
print(rate_limiter.allow_request(1))
time.sleep(1)
print(rate_limiter.allow_request(2))
time.sleep(1)
print(rate_limiter.allow_request(1))
time.sleep(1)
print(rate_limiter.allow_request(2))
time.sleep(1)
print(rate_limiter.allow_request(1))
time.sleep(1)
print(rate_limiter.allow_request(2))
time.sleep(1)
print(rate_limiter.allow_request(1))
time.sleep(1)
print(rate_limiter.allow_request(2))