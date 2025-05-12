import time

start_time = time.time()
# Code to be timed
time.sleep(2)  # Simulating a delay of 2 seconds
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")