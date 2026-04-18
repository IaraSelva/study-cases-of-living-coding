# You need to build an in-memory Currency Conversion Service that is:

# Correct – returns the right converted amount.
# Cached – avoids repeated slow “remote” calls.
# Thread-safe – safe if many threads call it concurrently.

# Requirements
# We’ll give you this function (pretend it’s a slow HTTP call):

# def fetch_rate(from_cur: str, to_cur: str) -> float:
#     """
#     Simulates a network request to get FX rate.
#     For our test it just looks up a static table, but *assume* it takes 100 ms.
#     """

# Your job:
# class CurrencyConverter:
#     def convert(self, amount: float, from_cur: str, to_cur: str) -> float:
#         """Returns amount * FX_rate, rounded to 4 dp."""
# Cache each rate for 10 seconds (TTL).

# If two threads ask for the same pair while the first is still fetching, only one call to fetch_rate should happen (others must wait or reuse).
# If from_cur == to_cur, return the original amount immediately.
# Handle unknown currency pairs by raising ValueError.
# Keep the public API minimal (just convert is OK).

import datetime
import threading

class Cache:
    def __init__(self):
        self.cache = {} # {(from_curr, to_curr): (rate, timestamp)}
        self.cache_time = datetime.timedelta(seconds=10) 
        self.round_precision = 4
        self.lock = threading.Lock()
    
    def get_currency_conversion(self, amount: float, from_curr: str, to_curr: str) -> float:
        if from_curr == to_curr: return amount

        # check if there's a cache value to return
        if (from_curr, to_curr) in self.cache:
            time_cache = self.cache[(from_curr, to_curr)][1]

            # check if the time is no older than 10 seconds ago
            if self.cache_has_expired(cache_time=time_cache):
                # call the API and update the cache
                try:
                    rate = self.call_rate_api(from_curr, to_curr)
                    self.set_cache(rate=rate, from_curr=from_curr, to_curr=to_curr)
                except ValueError:
                    pass        
        else:
            # Call the API and add it within cache
            try:
                rate = self.call_rate_api(from_curr, to_curr)
                self.set_cache(rate=rate, from_curr=from_curr, to_curr=to_curr)
            except ValueError as ex:
                raise ex
            
        return self.get_cache(current_currency=from_curr, converted_currency=to_curr, amount=amount)
                
    def call_rate_api(self, from_curr, to_curr):
        api_response_rate = api.fetch_rate(from_curr, to_curr)
        if not api_response_rate:
            raise ValueError(422, "Error converting rate")
        else:
            return api_response_rate
    
    def cache_has_expired(self, cache_time) -> bool:
        return datetime.datetime.now() - cache_time > self.cache_time
    
    def set_cache(self, rate, from_curr, to_curr):
        with self.lock:
            self.cache[(from_curr, to_curr)] = (rate, datetime.datetime.now())
    
    def get_cache(self, current_currency, converted_currency, amount):
        with self.lock:
            cache_rate = self.cache[(current_currency, converted_currency)][0]
            return self.convert_amount(cache_rate, amount)

    def convert_amount(self, rate, amount):
            return round(rate * amount, self.round_precision)




