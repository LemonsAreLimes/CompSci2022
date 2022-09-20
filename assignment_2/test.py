import time

for i in range(1000):
    time.sleep(0.01)

    print(i, end='\r')