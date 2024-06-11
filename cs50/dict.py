#list of dictionaries

students = [{'name':'Harry','house':'Gryffindor','Patronus':'Stag'},
            
            {'name':'Draco','house':'Slytherin','Patronus':None},
            {'name':'Hermione','house':'Gryffindor','Patronus':'Otter'},
            {'name':'Ron','house':'Gryffindor','Patronus':'Terrier'},]

for student in students:
  print(student['name'], student['house'], student['Patronus'], sep=' , ')