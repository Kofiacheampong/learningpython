def main():
   x = square(int(input('What is x?: ')))
   print (f'x squared is {x}')

def square(n):
   return n*n

if __name__ == '__main__':
    main()