#a way to creates lists with less syntax, can mimic certain lambda functions 

# squares = [i * i for i in range (1,5)]
# print (squares)


students = [100, 90, 59,70,45,56]
#passed =list(filter(lambda x: x>=60, students))
passed = [i if i >= 60 else 'FAILED' for  i in students ]
print(passed)