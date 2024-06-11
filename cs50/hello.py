# name = input('what is your name: ').strip().title()
# #remove whitespace from a str and capitalize each word
# #split user name to first and last
# first, last = name.split(' ')
# print(f'hello, {last}')

def main():
  name = input('What is your name?: ' )
  print(hello(name))


def hello(to = 'world' ):
  return f'hello {to}'
