import os
import time
re=os.fork()
if re==0:
    while True:
        print('---1---')
        time.sleep(1)
else:
    while True:
        print("---2----")
        time.sleep(1)