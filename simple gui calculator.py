from tkinter import *
import webbrowser

def getnum(num):
    cal.insert(END, num)

def delt():
    cal.delete(0, END)

def add():
    import re
    xx = cal.get()

    try:
        if xx.strip().lower() == "rick":
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=2)
            cal.delete(0, END)
            cal.insert(0, "Enjoy 😏")
            return
    except Exception:
        pass

    expr = xx.replace('x', '*').replace('×', '*').replace('÷', '/')

    if not re.fullmatch(r"[0-9+\-*/().\s]+", expr):
        cal.delete(0, END)
        cal.insert(0, "Error")
        return

    try:
        result = eval(expr, {"__builtins__": None}, {})
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        cal.delete(0, END)
        cal.insert(0, str(result))
    except Exception:
        cal.delete(0, END)
        cal.insert(0, "Error")




cw = Tk()
cw.title('CALCULATOR')
cw.geometry('300x400')
cw.resizable(0,0)
cw.config(bg='black')

cal = Entry(font='Arial 21', bd=10, width=30, bg='lightgrey', fg='red')
cal.pack()

btn1 = Button(text='7', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(7))
btn1.place(x=10, y=60)
btn2 = Button(text='8', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(8))
btn2.place(x=85, y=60)
btn3 = Button(text='9', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(9))
btn3.place(x=160, y=60)
btn4 = Button(text='4', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(4))
btn4.place(x=10, y=145)
btn5 = Button(text='5', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(5))
btn5.place(x=85, y=145)
btn6 = Button(text='6', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(6))
btn6.place(x=160, y=145)
btn7 = Button(text='1', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(1))
btn7.place(x=10, y=230)
btn8 = Button(text='2', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(2))
btn8.place(x=85, y=230)
btn9 = Button(text='3', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(3))
btn9.place(x=160, y=230)
btn0 = Button(text='0', font='Arial 19 bold', bg='white', bd=10, padx=10, pady=5, command=lambda: getnum(0))
btn0.place(x=10, y=320)

btnx = Button(text='+', font='Arial 19 bold', bg='lightgreen', height='1', bd=10, padx=10, pady=5, command=lambda: getnum('+'))
btnx.place(x=235, y=60)
btnminus = Button(text='- ', font='Arial 19 bold', bg='pink', bd=10, padx=10, pady=5, command=lambda: getnum('-'))
btnminus.place(x=235, y=145)

btnc = Button(text='C', font='Arial 19 bold', bg='crimson', height='1', width=2, bd=10,  padx=10, pady=4, command=delt)
btnc.place(x=85, y=320)
btnxxx = Button(text='÷', font='Arial 19 bold', bg='purple', height='1', bd=10,  padx=10, pady=4, command=lambda : getnum('÷'))
btnxxx.place(x=160, y=320)
btne = Button(text='=', font='Arial 19 bold', bg='khaki',  bd=10, padx=10, pady=5, command=add)
btne.place(x=235, y=320)
btnex = Button(text='x', font='Arial 19 bold', bg='blue', bd=10, padx=10, pady=5, command=lambda : getnum('x'))
btnex.place(x=235, y=230)

cw.mainloop()
