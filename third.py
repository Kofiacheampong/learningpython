# import os

# path = "/Users/kofiarcher/Desktop/recipes"

# if os.path.exists(path):
#    print('That location exists')
#    if os.path.isfile(path):
#       print('This is a file')
#    elif os.path.isdir(path):
#       print('this is a directory')
# else:
#    print('That location does not exist')

#try:
   # with open('swordfish.py') as file:
   #  print (file.read())
#except FileNotFoundError:
 #  print('that file was not found')

text = 'Nice to meet you Nigga.\n Have a nice day'

with open('test.txt', 'w') as file :
  file.write(text)


