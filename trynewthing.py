from tkinter import *
from tkinter import ttk
import time
root = Tk()
# root.geometry("400x100")#gives the shape of your page
# label1=Label(root,text="Enter")#gives the label
# ent=Entry(root)#provides text box
# label1.grid(row=0)
# ent.grid(row=0,column=1)
# button=Button(root,text="Search",bg="lightblue")#provides the button
# button.grid(row=2,columnspan=2)
# text=Text(root,width=100,height=30)#provides the bottom textbox
# text.grid(row=3,columnspan=8)
# root.mainloop()#form the entire requirements


 
#root.state("zoomed")  #to make it full screen
root.title("GUI")
root.configure(bg="DarkOrchid4")
 
main_menu = Menu(root)
root.config(menu=main_menu)
#window size
root.geometry("600x400")
 
#frame
frame=Frame(root)
 
 
Menu1=Menu(main_menu)
main_menu.add_cascade(label="M1", menu=Menu1)
 
#exit
Menu1.add_separator()
Menu1.add_command(label="Exit", command=root.quit)
 
 
 
Menu2=Menu(main_menu)
main_menu.add_cascade(label="TM2", menu=Menu2)
 
 
 
Menu3=Menu(main_menu)
main_menu.add_cascade(label="SM3", menu=Menu3)
 
 
 
Menu4=Menu(main_menu)
main_menu.add_cascade(label="M4", menu=Menu4)
 
 
 
topFrame = Frame(root, width=1350, height=50)  # Added "container" Frame.
topFrame.pack(side=TOP, fill=X, expand=1, anchor=N)
 
titleLabel = Label(topFrame, font=('arial', 10, 'bold'),bg="white",
                   text=" GUI",
                   bd=5, anchor=W)
titleLabel.pack(side=LEFT)
 
 
 
 
 
clockFrame = Frame(topFrame, width=100, height=50, bd=4, relief="ridge")
clockFrame.pack(side=RIGHT)
clockLabel = Label(clockFrame, font=('arial', 10, 'bold'), bd=5, anchor=E)
clockLabel.pack()
 
Bottom = Frame(root, width=1350, height=50, bd=4, relief="ridge")
Bottom.pack(side=BOTTOM, fill=X, expand=1, anchor=S)
 
def tick(curtime=''):  #acts as a clock, changing the label when the time goes up
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clockLabel.config(text=curtime)
    clockLabel.after(200, tick, curtime)
tick()  #start clock
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='text1')
        self.lbl2=Label(win, text='text2')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
         
        self.btn1=Button(win, text='Search by text1')
        self.btn2=Button(win, text='Find by text2')
         
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
         
        self.b1=Button(win, text='Search by text1', command=self.add)
        self.b2=Button(win, text='Find by text2')
         
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=250, y=150)
         
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
         
         
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))
        
mywin=MyWindow(root)
root.mainloop()