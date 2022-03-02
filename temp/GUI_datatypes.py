import tkinter as tk

win=tk.Tk()

############## double to float #####################
doubleData=tk.DoubleVar()
print(doubleData.get())
doubleData.set(2.4)
print(type(doubleData))

add_doubles=1.2222222222222222222222222+doubleData.get()
print(add_doubles)
print(type(add_doubles))

############## string var #####################
strData=tk.StringVar()
strData.set('Hello StringVar')
varData=strData.get()
print(varData)
print(type(varData))

############## int, double, boolean #####################
print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())

############## tkinter var #####################
intData=tk.IntVar()
print(intData)
print(intData.get())
print() #debug point