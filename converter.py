#importing Tkinter and necessary libraries for the project
from tkinter import *
from tkinter import messagebox


#defining Window
root=Tk()
root.geometry("300x400")
root.title("Temp Converter")
root.resizable(0,0)

#creating a list of tuples containing temperature measuring unit and their value 
Units=[
    ("Fahrenheit","F"),
    ("Celsius","C"),
    ("Kelvin","K")
]


#defining variable for radio button values
b = StringVar()
t= StringVar()
b.set(0)
t.set(0)


#choosing base
Base=Label(root,text="Choose Conversion From:").grid(row=0,sticky=W)
#using for loop to generate radiobuttons
pos=1
for text,val in Units:
    Radiobutton(root,text=text,value=val,variable=b).grid(row=pos,sticky=W)
    pos=pos+1


#choosing conversion to
To=Label(root,text="Choose Conversion To:").grid(row=4,sticky=W)
#using for loop to generate radiobuttons
pos=5
for text,val in Units:

    Radiobutton(root,text=text,value=val,variable=t).grid(row=pos,sticky=W)
    pos=pos+1

#text area to get input 
Label(root,text="Enter value").grid(row=8,column=0)
inp= StringVar()
inp.set('')
input=Entry(root,textvariable=inp,borderwidth=5).grid(row=9,column=0)


#conversion functions
def FtoC(value):
    return ((value-32)*5/9)
def CtoF(value):
    return((value*9/5)+32)
def CtoK(value):
    return (value+273.15)
def KtoC(value):
    return (value-273.15)
def FtoK(value):
    return((value-32)*5/9+273.15)
def KtoF(value):
    return((value-273.15)*9/5+32)



#OUTPUT Field
Label(root,text="Answer").grid(row=10,column=0)
out= StringVar()
output=Entry(root,textvariable=out,borderwidth=5).grid(row=11,column=0)


#defining converter logic
def click():
    out.set('')
    try:
        val=float(inp.get())
    except Exception as e:
        messagebox.showerror("Error","NOT A NUMBER")

    base=b.get()
    to=t.get()
    if(base==0 or to==0):
        messagebox.showerror("Error","CHOOSE CONVERSIONS")
    else:
         if(base==to):
             out.set(val)
         if(base=='F' and to=='C'):
            ans=FtoC(val)
            ans="%.2f" % ans
            out.set(ans)
         if(base=='C' and to=='F'):
            ans=CtoF(val)
            ans="%.2f" % ans
            out.set(ans)
         if(base=='C' and to=='K'):
            ans=CtoK(val)
            ans="%.2f" % ans
            out.set(ans)
         if(base=='K' and to=='C'):
            ans=KtoC(val)
            ans="%.2f" % ans
            out.set(ans)
         if(base=='F' and to=='K'):
            ans=FtoK(val)
            ans="%.2f" % ans
            out.set(ans)
         if(base=='K' and to=='F'):
            ans=KtoF(val)
            ans="%.2f" % ans
            out.set(ans)

#function to clear
def clear():
    b.set(0)
    t.set(0)
    inp.set('')
    out.set('')

#Calculate button
button1=Button(root,text='Calculate',command=click,padx=20,pady=10).grid(row=12,column=0)

#Clear button
button2=Button(root,text='Clear',command=clear,fg="white",bg="red").grid(row=12,column=1)

root.mainloop()