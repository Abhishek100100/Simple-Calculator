#CALCULATOR

from tkinter import *
root =Tk()

#TITLE for the window
root.title('Calculator')
large_font = ('Helvetica',19)
e = Entry(root,borderwidth =10,bg = '#EAECEE',font = large_font)
e.grid(row = 0,column = 0,columnspan = 4)


#Functions
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global operation
    operation = 'Addition'
    f_num = int(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_num
    global operation
    operation = 'Substraction'
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    global operation
    operation = 'Multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global operation
    operation = 'Division'
    f_num = int(first_number)
    e.delete(0, END)

def button_exp():
    first_number = e.get()
    global f_num
    global operation
    operation = 'Exponent'
    f_num = int(first_number)
    e.delete(0, END)

def button_sqrt():
    first_number = e.get()
    global f_num
    global operation
    operation = 'sqrt'
    f_num = int(first_number)
    e.delete(0, END)

def button_square():
    first_number = e.get()
    global f_num
    global operation
    operation = 'square'
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number  =e.get()
    e.delete(0,END)
    if operation == 'Addition':
        e.insert(0,f_num + int(second_number))
    elif operation == 'Substraction':
        e.insert(0, f_num - int(second_number))
    elif operation == 'Multiplication':
        e.insert(0, f_num * int(second_number))
    elif operation == 'Division':
        e.insert(0, f_num / int(second_number))
    elif operation == 'Exponent':
        e.insert(0, f_num ** int(second_number))
    elif operation == 'square':
        e.insert(0, f_num ** 2)
    elif operation == 'sqrt':
        e.insert(0, f_num ** 0.5)
    else: return (0)


#buttons
button1 = Button(root,text = 1,padx = 30,pady = 20,bg = '#AAB7B8',command =lambda: button_click(1)).grid(row =4 ,column =0)
button2 = Button(root,text = 2,padx = 30,pady = 20,bg = '#AAB7B8',command =lambda: button_click(2)).grid(row =4 ,column = 1)
button3 = Button(root,text = 3,padx = 30,pady = 20,bg = '#AAB7B8',command = lambda: button_click(3)).grid(row =4 ,column = 2)

button4 = Button(root,text = 4,padx = 30,pady = 20,bg = '#AAB7B8',command = lambda: button_click(4)).grid(row =3,column =0)
button5 = Button(root,text = 5,padx = 30,pady = 20,bg = '#AAB7B8',command = lambda: button_click(5)).grid(row =3,column =1)
button6 = Button(root,text = 6,padx = 30,pady = 20,bg = '#AAB7B8',command = lambda: button_click(6)).grid(row =3,column =2)

button7 = Button(root,text = 7,padx = 30,pady = 20,bg = '#AAB7B8',command = lambda: button_click(7)).grid(row =2,column =0 )
button8 = Button(root,text = 8,padx = 30,pady = 20,bg = '#AAB7B8',command = lambda: button_click(8)).grid(row =2,column =1)
button9 = Button(root,text = 9,padx = 30,pady = 20,bg = '#AAB7B8',command = lambda: button_click(9)).grid(row =2,column =2)

button0 = Button(root,text = 0,padx = 30,pady = 20,bg = '#AAB7B8',command = lambda: button_click(0)).grid(row =5,column =1)
button_clr = Button(root,text ='clear',padx = 20,pady = 20,bg= '#808B96',command =button_clear).grid(row =5,column =0)

button_add = Button(root,text ='+',padx = 29,pady = 20,bg = '#CACFD2',command =button_add).grid(row =3,column =3)
button_sub = Button(root,text ='-',padx = 30,pady = 20,bg = '#CACFD2',command =button_sub).grid(row =4,column =3)
button_mul = Button(root,text ='X',padx = 30,pady = 20,bg = '#CACFD2',command =button_mul).grid(row =2,column =3)
button_div = Button(root,text ='/',padx = 30,pady = 20,bg = '#CACFD2',command =button_div).grid(row =1,column =3)
button_exp = Button(root,text ='exp',padx = 23,pady = 20,bg = '#CACFD2',command =button_exp).grid(row =1,column =2)
button_square = Button(root,text ='Sq',padx = 27,pady = 20,bg = '#CACFD2',command =button_square).grid(row =1,column =0)
button_sqrt = Button(root,text ='SqRt',padx = 21,pady = 20,bg = '#CACFD2',command =button_sqrt).grid(row =1,column =1)


button_eq = Button(root,text = '=',padx = 72,pady = 18,bg = '#808B96',command =button_equal).grid(row =5,column = 2,columnspan =2)

root.mainloop()