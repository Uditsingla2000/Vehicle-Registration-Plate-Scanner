from tkinter import *
from tkinter import messagebox
#importing required Libraries

def validateLogin():
    if password.get() =='1234':
        #password is set to 1234 
        loginlabel = Label(tkWindow, text="Login successful",pady=10,fg="green").place(x= 100,y= 200)
        messagebox.showinfo("Success","Login Successful")
        tkWindow.destroy()
        print("username entered :", username.get())
        print("password entered :", password.get())
        import ocr
        #importing the ocr.py file and executing it at the same time
    else:
        loginlabel1 = Label(tkWindow, text="Login unsuccessful",pady=10,fg="red").place(x= 100,y= 200)
        messagebox.showerror("Failed","Login Unnuccessful")
    
    return

#window
tkWindow = Tk()  
tkWindow.geometry('320x300')  
tkWindow.title('Login Form')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name: ").place(x= 30,y= 30)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=105,y=30)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password: ").place(x= 30,y=70 )
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x=105,y=70)  


#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).place(x= 95,y= 110)  

tkWindow.mainloop()