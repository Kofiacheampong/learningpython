import re

email = input('whats your email?: ').strip()

if re.search(r'.+@.+\.edu',email):
  print('Valid')
else:
  print('Invalid')

