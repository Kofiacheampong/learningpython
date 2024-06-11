from tkinter import *
# widgets = GUI elements: buttons text boxes, labels, images
# windows = containers for widgets

window = Tk() #instantiate an instance of a window
window.title('First GUI program')

# logo = PhotoImage (file = 'SwiftLineAsset 5.png')
count = 0
photo = PhotoImage(file='man.png')

# window.iconphoto(True, logo)
# window.config(background='white')

# label =Label(window, text= 'Hello, bro do you even code?', 
#              font=('Arial', 40, 'bold'), 
#              fg='blue', 
#              bg='white',
#              relief=RAISED,
#              bd= 5,
#              padx=10,
#              pady=10,
#             image=photo,
#             compound='bottom')
# label.pack()
# #label.place(x,y)
def click():
  global count
  count+=1
  print(count)
button = Button(window,
                text=' Click me ',
                command= click,
                bg='black',
                font=('Comic Sans', 30),
                fg='green',
                activebackground='black',
                activeforeground='white',
                state=ACTIVE,
                image=photo,
                compound= 'top')
button.pack()

window.mainloop()


