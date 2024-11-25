from tkinter import *

root = Tk()
root.title("Packing in Tkinter")
root.geometry("650x650+650+150")
root.config(bg="#6FAFE7")

#Arrange button widget using pack
btn1 = Button(root, text="Click me")
btn1.pack(side="left")

#Arrange Label using pack
lbl1 = Label(root, text="Ek is n nar", bg="skyblue")
lbl1.pack(side="right")
lbl2 = Label(root, text="Hallo", bg="purple", fg="white", relief="sunken")#Avail relief's: flat|raise|sunken|groove|ridge
lbl2.pack(side="right", ipady=5, fill='y')
lbl2.config(font=("Times New Roman", 30))#Change font of widget

#Define testing function for check box
def toggled():
    print("The check button works.")

#Define vasriable to check if checkbox is checked
var = IntVar()
chk = Checkbutton(root, text="Click me", bg="skyblue", command=toggled, variable=var)
chk.pack(side="bottom")


def checkInput():
    '''check that the username and password match'''
    usernm = "Testing"
    pswrd = "Testing123"
    entered_usernm = usernameEntry.get()  # get username from Entry widget
    entered_pswrd = passEntry.get()  # get password from Entry widget

    if (usernm == entered_usernm) and (pswrd == entered_pswrd):
        print("Login successfull")
        root.destroy()  

    else:
        print("Login failed: Invalid username or password.")

def toggled():
    '''display a message to the terminal every time the check button
    is clicked'''
    print("The check button works.")

userFrame = Frame(root, bg="#32414e")
userFrame.pack(side='top')

Label(userFrame, text="Username: ", bg="#6FAFE7").pack(side='left', padx=5)

usernameEntry = Entry(userFrame, bd=3)
usernameEntry.pack(side='right')

passFrame = Frame(root, bg="#e5ff00")
passFrame.pack(side='top')

Label(passFrame, text="Password: ", bg="#6FAFE7").pack(side='left', padx=5)

passEntry = Entry(passFrame, bd=3)
passEntry.pack(side='right')

#Create Go button
btnGo = Button(root, text="Go", command=checkInput, bg="#6FAFE7")
btnGo.pack(pady=5)


# Remember me and forgot password
bottom_frame = Frame(root, bg="#6FAFE7")
bottom_frame.pack()

var = IntVar()

remember_me = Checkbutton(bottom_frame, text="Remember me", bg="#6FAFE7", command=toggled, variable=var)
remember_me.pack(side='left', padx=19)

# The forgot password Label is just a placeholder, has no function currently
forgot_pswrd = Label(bottom_frame, text="Forgot password?", bg="#6FAFE7")
forgot_pswrd.pack(side="right", padx=19)


root.mainloop()