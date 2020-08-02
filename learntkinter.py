import sys
from tkinter import *

class mydata(object):
	"""docstring for mydata"""
	def __init__(self, credit,lis):
		# super(mydata, self).__init__()
		self.credit = credit
		self.coins=0
		self.prices=lis
	# credit = 0
	# coins = 0
	# choice = 0
	# credit1 = 0
	# coins = 0
	# prices = [200,150,160,50,90]

def insert():
    insert = Tk()

    insert.geometry("450x250")
    iLabel = Label(insert, text="Enter coins.[Press Buttons]").grid(row=1, column=1)

    # tenbutton = Button(insert, text="10p").grid(row=2, column=1)
    tenbutton = Button(insert, text="10p", command=tenbuttonCallback)
    tenbutton.grid(row=2, column=1)
    twentybutton = Button(insert, text="20p",command=tenbuttonCallback).grid(row=3, column=1)
    fiftybutton = Button(insert, text="50p").grid(row=4, column=1)
    poundbutton = Button(insert, text="£1").grid(row=5, column=1)
    # insert.mainloop()
class createlis:
	lis=[200,150,160,50,90]
	def __init__(self,lis):
		self.createdlis=lis
myclass=mydata(0,createlis.lis)
print(createlis.lis)
k=createlis(9)
print(k.createdlis)
print(k.lis)
def tenbuttonCallback():
    # global credit
    # credit += 10
    myclass.credit+=10
    print(myclass.credit)
    print(myclass.coins)
    print(myclass.prices)
insert()



# from tkinter import *
# import tkinter
# import tkinter.messagebox

# root = Tk()


# def fun(arg):
#     if arg == 1:
#         tkinter.messagebox.showinfo("button 1", "button 1 used")
#     elif arg == 2:
#         tkinter.messagebox.showinfo("button 2", "button 2 used")
#     elif arg == 3:
#         tkinter.messagebox.showinfo("button 3", "button 3 used")
#     elif arg == 4:
#         tkinter.messagebox.showinfo("button 4", "button 4 used")


# b1 = Button(root, text="Quit1", command=lambda: fun(1))
# b1.pack()
# b2 = Button(root, text="Quit2", command=lambda: fun(2))
# b2.pack()
# b3 = Button(root, text="Quit3", command=lambda: fun(3))
# b3.pack()
# b4 = Button(root, text="Quit4", command=lambda: fun(4))
# b4.pack()

# root.mainloop()