import time

#print(time.ctime(0 )) #convert a time expressed in seconds since epoch to readable epoch = when your computer thinks time began

#print(time.time()) #return current seconds since epoch

print(time.ctime(time.time()))

time_object = time.localtime()

print (time_object)
local_time =time.strftime('%B-%d-%Y %H:%M:%S', time_object)

print (local_time)
