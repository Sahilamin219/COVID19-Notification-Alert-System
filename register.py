from tkinter import *
import os
 
creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'
 
def Signup():
    global pwordE
    global nameE
    global roots
 
    roots = Tk() 
    roots.title('Signup')
    roots.geometry('550x250')
    intruction = Label(roots, text='Please Enter new Credidentials\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(roots, text='New Username: ')
    pwordL = Label(roots, text='New Password: ') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W)
 
    nameE = Entry(roots).grid(row=1, column=1)
    pwordE = Entry(roots, show='*').grid(row=2, column=1)
 
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()
 
def FSSignup():
    with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.close() # Closes the file
 
    roots.destroy() # This will destroy the signup window. :)
    Login() # This will move us onto the login definition :D
 
def Login():
    global nameEL
    global pwordEL
    global rootA
 
    rootA = Tk() 
    rootA.title('Login') 
    rootA.geometry('450x250')
    intruction = Label(rootA, text='Please Login\n')
    intruction.grid(sticky=E) 
 
    nameL = Label(rootA, text='Username: ') 
    pwordL = Label(rootA, text='Password: ') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
 
    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) # This makes the deluser button. blah go to the deluser def.
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        r = Tk() # Opens new window
        r.title(':D')
        r.geometry('250x150') # Makes the window a certain size
        rlbl = Label(r, text='\n[+] Logged In') # "logged in" label
        rlbl.pack() # Pack is like .grid(), just different
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('250x150')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
 
def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() # Destroys the login window
    Signup() # And goes back to the start!
 
if os.path.isfile(creds):
    Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()

# from tkinter import *
# from tkinter import ttk
# window = Tk()
# window.title("Please Register")
# window.geometry('400x400')
# window.configure(background = "gray")
# ttk.Button(window, text="Hello, User!").grid()
# a = Label(window ,text = "First Name").grid(row = 1,column = 0)
# b = Label(window ,text = "Last Name").grid(row = 2,column = 0)
# c = Label(window ,text = "Email Id").grid(row = 3,column = 0)
# d = Label(window ,text = "Contact Number").grid(row = 4,column = 0)
# a1 = Entry(window).grid(row = 1,column = 1)
# b1 = Entry(window).grid(row = 2,column = 1)
# c1 = Entry(window).grid(row = 3,column = 1)
# d1 = Entry(window).grid(row = 4,column = 1)
# def clicked():
#    res = "Stay Home Stay Safe" #+ txt.get()
#    lbl.configure(text= res)
# btn = ttk.Button(window ,text="Submit",command=clicked).grid(row=5,column=0)
# window.mainloop()
# window.mainloop()