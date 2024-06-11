name = input('What is your name? ')
print(f'Welcome {name}, to this adventure')

answer = input('Would you like to go right or left?: ')

if answer == 'right':
  answer = input('You have come to a bridge, cross or go back. Type cross or go-back: ')
  if answer == 'go-back':
    print('Pussy you lose')
  elif answer == 'cross':
    answer = input('You meet a stranger. Talk or Ignore')
    if answer == 'Talk':
      print('You in an pot of gold')
  else:
      print('You lose') 

elif answer == 'left':
  answer = input('You come to a river, type walk to use the path or swim to go across')
  if answer == 'swim':
    print('You swam across and got eaten by an alligator.')
  elif answer == 'walk':
    print('You run out of water ')
  else: 
    print('You lose')

  