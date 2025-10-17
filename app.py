import time
import datetime

# Infinite loop to keep container alive
while True:
    print(f"{datetime.datetime.now()}: Container is alive!", flush=True)
    time.sleep(5)
