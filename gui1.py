from tkinter import *
import tkinter 
import webbrowser
def a():
	top=tkinter.Tk()
	w=tkinter.Button(top,text="cse ds&aiml",height=1,width=10,activebackground="green",activeforeground="blue",command=ds1)
	w.pack()
	top.geometry("250x300")
	top.mainloop()
def ds1():
	top=tkinter.Tk()
	w=tkinter.Button(top,text="1-1",width=10,command=ds2)
	w2=tkinter.Button(top,text="1-2",width=10)
	w3=tkinter.Button(top,text="2-1",width=10)
	w.pack()
	w2.pack()
	w3.pack()
	top.geometry("250x300")
	top.mainloop()
def ds2():
	top=tkinter.Tk()
	w=tkinter.Button(top,text="m-1",width=10,command=maths)
	w1=tkinter.Button(top,text="english",width=10)
	w2=tkinter.Button(top,text="dld",width=10)
	w3=tkinter.Button(top,text="c lang",width=10)
	w4=tkinter.Button(top,text="bee",width=10)
	w.pack()
	w2.pack()
	w3.pack()
	top.geometry("250x300")
	top.mainloop()
def maths():
	top=tkinter.Tk()
	var=StringVar()
	w=tkinter.Label(top,textvariable=var,width=100,relief=RAISED)
	var.set=("unit 1-matrices")
	w1=tkinter.Button(top,text="click here",command=link1)
	w.pack()
	w1.pack()
	top.geometry("250x300")
	top.mainloop()
def link1():
	webbrowser.open("https://www.youtube.com/watch?v=RtuNwdHDEAw&list=PLKS7ZMKnbPrT-Gy4k0r8jAr0mX2K32yyV")
a()