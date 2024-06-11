import csv
name = input ('What is your name?: ')
home = input ('Where is your home?: ')

with open ('students.csv','a') as file:
  writer = csv.DictWriter(file, fieldnames=['name', 'home'])
  writer.writerow({'name':name, 'home':home})








# students =[]

# with open ('students.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({'name': row['name'], 'home':row['home']})

#   #      name, house = line.rstrip().split(',')
#   #      student={'name': name, 'house':house}


# # def get_name(student):
# #     return student['name']


# for student in sorted(students, key= lambda student: student['name'], reverse=True):
#     print(f"{student['name']} is from  {student['home']}")