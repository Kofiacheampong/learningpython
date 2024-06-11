#threads that run in the background and are not important for program to run
#non daemon threads usually cannot be killed until the task is complete
#background tasks, garbage collection, waiting for user input

import threading
import time

def timer():
  print()
  count = 0
  while True:
    time.sleep(1)
    count +=1
    print('logged in for: ', count , 'seconds')

x = threading.Thread(target=timer, args=(), daemon= True)
x.start()

answer = input('Do you wish to exit?: ')