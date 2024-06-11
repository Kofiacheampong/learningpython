#creates a collection of elements from an iterable for which a function returns

friends = [('Rachel',20),
           ('Josh',17),
           ('Ramon',16),
           ('Rachel',20),
           ('Hayat',29)]

age = lambda data: data[1] >= 18 

drinking_buddies =list(filter(age, friends))

for i in drinking_buddies:
  print (i)