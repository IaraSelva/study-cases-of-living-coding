# Implement a class TransactionAggregator that supports:

# ✅ add_transaction(user_id: str, amount: float)
# Adds a transaction for the given user.

# ✅ get_total(user_id: str) -> float
# Returns the sum of all transactions for that user.

# ✅ get_average(user_id: str) -> float
# Returns the average transaction amount for that user.

import threading
from collections import defaultdict

class TransactionAggregator:
    def __init__(self):
        self.users_transactions = {}
        self.user_locks = defaultdict(threading.Lock)

    def add_transaction(self, user_id: str, amount: float) -> None:
        with self.user_locks[user_id]:
            user_amount_trans = self.users_transactions.setdefault(user_id, {
                "total_amount": 0.0,
                "n_transactions": 0
            })
            user_amount_trans["total_amount"] += amount
            user_amount_trans["n_transactions"] += 1
            print(f"threading {threading.current_thread().name} added {amount} to {user_id}. Total = {user_amount_trans["total_amount"]}")
    
    def get_total(self, user_id: str) -> float:
        return self.users_transactions.get(user_id, {}).get("total_amount", 0.0)
    
    def get_average(self, user_id: str) -> float | str:
        if user_id in self.users_transactions:
            total_amount = self.users_transactions[user_id].get("total_amount")
            n_transactions = self.users_transactions[user_id].get("n_transactions")
            if n_transactions == 0: return 0.0
            return round(total_amount/n_transactions, 2)
        return "User not found"

import time
import concurrent.futures

transaction = TransactionAggregator()
start = time.perf_counter()

def simulate_transactions(user_id, amount, times):
    for _ in range(times):
        transaction.add_transaction(user_id, amount)
        time.sleep(0.01)

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(simulate_transactions, "user_1", 10, 10)

    

# threads = []
# for i in range(5):
#     amount = [10,20,30,40,50]
#     t = threading.Thread(target=simulate_transactions, args=("user_1", amount[i], 5))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

end = time.perf_counter()
print(f"time spend = {end-start}")


# print(transaction.get_total(1))
# print(transaction.get_average(1))

# transaction.add_transaction(1, 45.00)
# transaction.add_transaction(1, 55.00)
# print(transaction.get_total(1))
# print(transaction.get_average(1))

# print(transaction.get_total(2))
# print(transaction.get_average(2))

# transaction.add_transaction(2, 150.00)
# transaction.add_transaction(2, 200.00)
# print(transaction.get_total(2))
# print(transaction.get_average(2))

