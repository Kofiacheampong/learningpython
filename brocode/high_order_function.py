# a function that either accepts a function as an argument or returns a function
# in python functions are treated as objects

def loud (text):
  return text.upper()

def quiet(text):
  return text.lower()

def hello (func):
  text=func('hello')
  print(text)

hello(loud)

def divisor(x):
  def dividend(y):
    return y/x
  return dividend

divide = divisor(2)
print (divide(10))