import tkinter as tk

me=tk.Tk()
me.geometry("345x460")
me.title("CALCULATOR")

melable=tk.Label(me,text="CALCULATOR",fg='white', bg='black', font=('Courier New', 30, 'bold')) 
melable.pack()
me.config(background='black')

textin=tk.StringVar()
operator=""

def clickbut(number):
  global operator
  operator=operator+str(number)
  textin.set(operator)

def equalbut():
  try:
   global operator
   eq=str(eval(operator))
   textin.set(eq)
   operator=""
  except ZeroDivisionError:
   textin.set('')
   operator=""
   e1.insert(0, "Err")

def ctrbut():
  global operator
  textin.set('')
  operator=""
  e1.insert(0, "0")

def DEL():
  length=len(e1.get())
  e1.delete(first=length-1,last=length)
  if length == 1:
    	global operator
    	textin.set('')
    	operator=""
    	e1.insert(0, "0")


e1=tk.Entry(me,font=('Courier', 16, 'bold'),fg='blue', textvar=textin, width=25, bd=5, bg="powder blue")
e1.place(x=5, y=50)


but1=tk.Button(me,padx=14, pady=14,command=lambda:clickbut(1), text="1",font=('Courier New', 16, 'bold'))
but1.place(x=10, y=100)

but2=tk.Button(me,padx=14, pady=14,command=lambda:clickbut(2), text="2",font=('Courier New', 16, 'bold'))
but2.place(x=10, y=170)


but3=tk.Button(me,padx=14, pady=14,command=lambda:clickbut(3), text="3",font=('Courier New', 16, 'bold'))
but3.place(x=10, y=240)

but4=tk.Button(me,padx=14, pady=14,command=lambda:clickbut(0), text="0",font=('Courier New', 16, 'bold'))
but4.place(x=10, y=310)




but5=tk.Button(me,padx=14, pady=14,command=lambda:clickbut(4), text="4",font=('Courier New', 16, 'bold'))
but5.place(x=75, y=100)


but6=tk.Button(me,padx=14, pady=14, command=lambda:clickbut(5), text="5",font=('Courier New', 16, 'bold'))
but6.place(x=75, y=170)

but7=tk.Button(me,padx=14, pady=14,command=lambda:clickbut(6), text="6",font=('Courier New', 16, 'bold'))
but7.place(x=75, y=240)

but8=tk.Button(me,padx=48, pady=14, command=lambda:clickbut("."), text=".",font=('Courier New', 16, 'bold'))
but8.place(x=75, y=310)


but9=tk.Button(me,padx=14, pady=14, command=lambda:clickbut(7),text="7",font=('Courier New', 16, 'bold'))
but9.place(x=140, y=100)

but10=tk.Button(me,padx=14, pady=14,command=lambda:clickbut(8), text="8",font=('Courier New', 16, 'bold'))
but10.place(x=140, y=170)

but11=tk.Button(me,padx=14, pady=14,command=lambda:clickbut(9), text="9",font=('Courier New', 16, 'bold'))
but11.place(x=140, y=240)

but12=tk.Button(me,padx=14, pady=14,command=lambda:clickbut("+"), text="+",font=('Courier New', 16, 'bold'))
but12.place(x=205, y=100)

but13=tk.Button(me,padx=14, pady=14, command=lambda:clickbut("-"), text="-",font=('Courier New', 16, 'bold'))
but13.place(x=205, y=170)

but14=tk.Button(me,padx=14, pady=14,command=lambda:clickbut("*"), text="x",font=('Courier New', 16, 'bold'))
but14.place(x=205, y=240)


but15=tk.Button(me,padx=14, pady=14,command=lambda:clickbut("/"), text="/",font=('Courier New', 16, 'bold'))
but15.place(x=205, y=310)

but16=tk.Button(me,padx=106, pady=14,command=ctrbut, text="CE",font=('Courier New', 16, 'bold'))
but16.place(x=75, y=380)

but17=tk.Button(me,padx=14, pady=14,command=equalbut, text="=",font=('Courier New', 16, 'bold'))
but17.place(x=10, y=380)



but18=tk.Button(me,padx=2, pady=120,command=DEL, text="DEL",font=('Courier New', 16, 'bold'))
but18.place(x=270, y=100)












tk.mainloop()