def main():
  prompt = input('enter your greeting: ')
  if 'hello' in prompt :
    print('$0')
  elif prompt.startswith('h'):
    print ('$20')
  else:
    print ('$100')



main()