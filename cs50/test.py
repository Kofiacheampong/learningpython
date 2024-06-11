from hello import hello
import pytest


# def test_square():
#   assert square(2)==4
#   assert square(3)==9
#   assert square(-3) == 9

# def test_str(): 
#   with pytest.raises(TypeError):
#     square('cat')

def test_default():
  assert hello() == 'hello world'

def test_argument():
  assert hello('Kofi') == 'hello Kofi'



