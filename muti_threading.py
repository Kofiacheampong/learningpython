# thread = a flow of execution like a separate order of instructions, however each thread takes a turn running to achieve concurrency
#GIL = (global interpreter lock ),
#allows only one thread to hold control of the python interpreter

#io bound program that spends most of its time waiting for external events like user inputs (multithreading)
# cpu bound = program that spends most of its time waiting for internal events (multiprocessing)

import threading
import time

print(threading.active_count())

def eat_breakfast():
  time.sleep(3)
  print('Eating')

def drink_coffee():
  time.sleep(4)
  print('drinking')

def study():
  time.sleep(3)
  print('sleeping')

x= threading.Thread(target= eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z= threading.Thread(target=study,args=())
z.start()

x.join( ) #main thread has to wait 

# eat_breakfast()
# drink_coffee() 
# study()

print(threading.enumerate())