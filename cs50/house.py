name = input('What is your name')
name = name.capitalize()


match name:
  case 'Harry' |'Hermione', 'Ron':
    print('Gryffindor')
  case 'Draco':
    print('Slytherin')
  case _:
    print('Get the fuck out', name)
 
