'''
Scenario: External Service Integration with Retries and Timeout
You’re building a backend service that depends on an external HTTP API to fetch exchange rates. Sometimes this API fails or takes too long. Your job is to design a robust way to call this external service, handling:

- Timeouts
- Retry with backoff
- Logging
- Max attempts

Assume you already have a function to make the raw HTTP call:

def fetch_rate_from_api(source: str, target: str) -> float:
    """
    Simulates a third-party call. It may:
    - return the exchange rate
    - raise TimeoutError
    - raise ConnectionError
    """
✅ Task
Implement a wrapper function:
def get_rate_with_retries(source: str, target: str) -> float:
    """
    Calls `fetch_rate_from_api` in a fault-tolerant way.
    Retries with exponential backoff (1s, 2s, 4s...).
    Max 3 attempts.
    Logs on failure.
    Raises exception if all attempts fail.
    """
Notes
Use time.sleep() for backoff.
Use print() for logging.
Feel free to simulate failures inside fetch_rate_from_api.

Bonus
Add a jitter to the backoff delay.
Accept max_attempts, base_delay, or logger as parameters.
'''
class CustomException(Exception):
    def __init__(self):
        self.message = "Timeout connection - The maximum retries has been exceeded"
        super().__init__(self.message)

import random
import time

class FetchRate:
    def __init__(self, max_attemps: int = 3, delay: int = 1):
        self.max_attempts = max_attemps
        self.delay = delay

    def get_rate_with_retries(self, source: str, target: str, attempt: int = 1) -> float:
        """
        Calls `fetch_rate_from_api` in a fault-tolerant way.
        Retries with exponential backoff (1s, 2s, 4s...).
        Max 3 attempts.
        Logs on failure.
        Raises exception if all attempts fail.
        """
        try:
            print("Trying established connection with the rate api")
            response = self.fetch_rate_from_api(source, target)
            print(f"API has successfully responds {response}")
            return response
        except (TimeoutError, ConnectionError):
            if attempt == self.max_attempts:
                print("Max attempts exceeded")
                raise CustomException()
            print("Waiting to retry calling the api")
            time.sleep(self.delay * 2 ** (attempt - 1))
            return self.get_rate_with_retries(source, target, attempt+1)


    def fetch_rate_from_api(self, source: str, target: str) -> float:
        """
        Simulates a third-party call. It may:
        - return the exchange rate
        - raise TimeoutError
        - raise ConnectionError
        """
        if source == "a":
            return round(random.random(), 2)
        if source == "b":
            raise TimeoutError
        if source == "c":
            raise ConnectionError

call_api = FetchRate()

call_api.get_rate_with_retries("c", "b")
