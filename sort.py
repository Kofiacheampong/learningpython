#sort () method = used with lists
#sort ()function = used with iterables

students = ['santo','okala','judas', 'agyakoo']

students.sort(reverse=True)

for i in students:
  print(i) 

dancers = (('santo','F',60),
           ('okala','C',80),
           ('judas','B',90))

grade = lambda grades: grades[2]
#dancers.sort(key = grade, reverse=True) #sorting lists
sorted_students= sorted(dancers, key=grade) #sorting iterables
for i in sorted_students:
  print(i)