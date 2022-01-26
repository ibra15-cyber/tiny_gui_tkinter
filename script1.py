from tkinter import *

window=Tk() #saving an obj Tk as window

def km_to_miles():
    # print(e1_value.get()) #that string is called here
    mile = float(e1_value.get())*1.6 #get the value entered in entry and multiply by 1.6
    t1.insert(END, mile) #insert it at the int in t1

b1=Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)



#will be expecting a string el_value
#in the entry field
e1_value=StringVar() 
e1=Entry(window, textvariable=e1_value) 
e1.grid(row=0, column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()