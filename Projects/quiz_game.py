print('Welcome to my quiz')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
  quit()
print('Okay lets play: ')
score = 0

answer = input ('What is the meaning of CPU? ')
if answer == 'central processing unit':
  print('Correct!')
  score += 1
else: 
  print('Wrong!')

answer = input ('What is RAM? ')
if answer == 'random access memory':
  print('Correct!')
  score += 1
else: 
  print('Wrong!')

answer = input ('What is the meaning of GPU? ')
if answer == 'graphics processing unit':
  print('Correct!')
  score += 1
else: 
  print('Wrong!')

answer = input ('What is the meaning of PSU? ')
if answer == 'power supply':
  print('Correct!')
  score += 1

else: 
  print('Wrong!')

print (f'You got {score/4 * 100}%')
