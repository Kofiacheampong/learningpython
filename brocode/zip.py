# zip(*iterables) = aggregate elements from two or more iterables, creates a zip object with paired elements stored in tuples for each element

usernames = ['dude', 'bro', 'nigga']
passwords =['password', 'abcd', 'please'] 
login_date =['1/1/21','2/2/22','3/12/23']
users = zip (usernames, passwords,login_date)

for i in users:
  print (i) 