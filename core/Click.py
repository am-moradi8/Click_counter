from tkinter import *
from tkinter import ttk
counter = 0
def count ():
    global counter
    counter += 1
    lb_1.config(text='count : {}'.format(counter) )
    
win = Tk()
win.title('project')
win.geometry('200x200')
win.config(bg='#16DED0')

lb_1 = Label(win , text=('Number of clicks :') ,fg='red' , bg='yellow' )
lb_1.place(x=75, y=75)


bt_1 = ttk.Button(win , text= 'Click here' , command= count )
bt_1.place(x=75, y=125)


win.mainloop()