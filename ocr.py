from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from progress import PSS
#importing required Libraries


root=Tk()
#starting a tKinter window
#giving it a title 
root.title("Number Plate Scanner")


def import_photo():
    global filename
    filename = filedialog.askopenfilename(title="Select Image",filetypes =(("jpg files","*.jpg"),("png files","*.png")))
    #selecting an image and storing its address in variable filename
    # print('Selected:', filename)
    # print(type(filename))
    global image1,my_imag1,my_img1  #making gloabal variables
    image1 =Image.open(filename)
    image1 = image1.resize((360, 250))
    my_img1 = ImageTk.PhotoImage(image1)
    my_imag1 = Label(image = my_img1,padx=10,pady=10,borderwidth=3, relief="solid")
    my_imag1.place(x=10,y=100)
    label1=Label(text="Selected Image :").place(x=110,y=75)
    #displaying the selected image and the Deetect plate function , which will call the scan_image function
    detect_plate =Button(text="Detect Plate",padx=7,pady=7, relief="ridge",command=lambda:scan_image(filename)).place(x=370,y=400)
    return

#Main window inital code, making a browse Button  
l1 = Label(text="Select Image")
l1.config(font =("Roboto", 12))
l1.place(x=140,y=20) 
browse =Button(text = 'Browse',padx=30,pady=7, relief="ridge",anchor=N,command=lambda:import_photo()).place(x=260,y=10)
#calling the import_photo function

def scan_image(filename):
    #this function will call the function in scanner.py and make a cropped photo of number plate and scan the number on the plate  
    try:
        global num
        import scanner
        num = scanner.newfunction(filename) 
        # print(num)
        cropped()
        #calling the cropped function to display the cropped number plate image and the scanned number  
    except Exception as e:
        print("An exception occurred: ", e) 
    
    return
    
def cropped():
    global image2,my_imag2,my_img2
    ps=PSS()
    image2 =Image.open("1.png")
    image2 = image2.resize((200, 80))
    my_img2 = ImageTk.PhotoImage(image2)
    my_imag2 = Label(image = my_img2,padx=10,pady=10,borderwidth=3, relief="solid")
    my_imag2.place(x=380,y=180)
    label2=Label(text="Cropped Image").place(x=400,y=155)
    but1 =Button(text="Show Details",padx=7,pady=7, relief="ridge",command=lambda:details(num)).place(x=480,y=400)
    T = Text(root,fg="red", height = 1, width = 20)
    T.place(x=140,y=410) 
    T.insert(INSERT, num)
    l = Label(text="Result")
    l.config(font =("Helvetica", 10,'bold')) 
    l.place(x=80,y=406)
    return
    
def details(num):
    num =num
    # ps=PSS()
    # but1.destroy()
    import aps
    aps.fun(num)
    # import_photo()
    return

# but2 =Button(text="Exit",padx=7,pady=7, relief="ridge",command=root.destroy()).place(x=480,y=10)   

root.geometry("600x500")
root.mainloop()


