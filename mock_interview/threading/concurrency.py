import time
import threading
import concurrent.futures

start = time.perf_counter()

def start_program(seconds):
    print(f"started in {round(start, 2)}")
    print(f"sleeping {seconds} sec...")
    time.sleep(seconds)
    return f"done sleeping {seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs_to_sleep = [5,4,3,2,1]
    #results = [executor.submit(start_program, sec) for sec in secs_to_sleep]
    results = executor.map(start_program, secs_to_sleep)
    
    # for future in concurrent.futures.as_completed(results):
    #     print(future.result())
    for result in results:
        print(result)

# list_threads = []

# for i in range(10):
#     i_thread = threading.Thread(target=start_program, args=[1.5])
#     i_thread.start()
#     list_threads.append(i_thread)

# for t in list_threads:
#     t.join()
    

finish = time.perf_counter()
print(f"finished at {round(finish, 2)}")

print(f"total time = {round(finish-start, 2)} seconds")