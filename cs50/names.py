names = []

# for _ in range (3):
#     names.append  (input('what is your name?: '))

# for name in sorted (names):
#     print(f'hello {name}')

# name = input('What is your name?: ')

# with open('names.txt', 'a') as file:
#     file.write(f'{name}\n')

with open ('names.txt') as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names, reverse= False):
  print(f'{name}')



# with open ('names.txt') as file:
#   for line in sorted(file):
#     print('hello', line.strip())
   