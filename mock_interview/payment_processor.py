# Design a class called PaymentProcessor that supports the following methods:
# process(payment_id: str) -> bool:
# Returns True if the payment was successfully processed.
# Returns False if the payment was already processed before.

# You don’t need to actually process anything — just simulate tracking whether a payment was already seen.

import threading
from threading import Lock
from collections import defaultdict
import datetime
from datetime import timedelta
import schedule

class PaymentProcessor:
    def __init__(self, time_to_live_hour: int = 24):
        self.transactions_id = set()
        self.transactions_lock = defaultdict(threading.Lock)
        self.transation_timestamp = {}
        self.timestamp_cleanup = datetime.timedelta(hours=time_to_live_hour)

    def proccess_payment(self, payment_id: str) -> bool:
        with self.transactions_lock[payment_id]:
            if payment_id in self.transactions_id:
                return False
            else:
                # proccess the transaction and add it to set
                self.transactions_id.add(payment_id)
                self.transation_timestamp[payment_id] = datetime.datetime.now()
            return True
        
    def clean_up(self, transaction_id, timestamp): # run this function once a day with a schedule when there's less transactions happening
        if timestamp - datetime.datetime.now() > self.timestamp_cleanup:
            with self.transactions_lock[transaction_id]:
                self.transactions_id.remove(transaction_id)

    def clen_in_paralell(self):
        threads = []
        for transaction_id, timestamp in self.transation_timestamp.items():
            t = threading.Thread(target=self.clean_up, args=(transaction_id, timestamp))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
    schedule.every().day.at("03:00").do(clen_in_paralell)

        
payment = PaymentProcessor()

# print(payment.proccess_payment(1))
# print(payment.proccess_payment(1))
# print(payment.proccess_payment(2))

import time
import concurrent.futures
def simulate_transactions(id, times):
    for i in range(times):
        print(payment.proccess_payment(id))

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.submit(simulate_transactions, "pay_1", 100)

end = time.perf_counter()

print(f"finished in {end-start} seconds")
