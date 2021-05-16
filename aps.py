#request module allow us to send HTTP requests using python
import requests
# pprint allows us to print our json data in a more organized manner
import pprint
#json module is used to convert our python dictionary into JSON string that can be wriiten in a text file
import json
#import ocr
import random
from tkinter import *
from tkinter import messagebox

#ocr.details()
def fun(num):
  # calling our API by implementing POST method
  r= requests.get('https://my.api.mockaroo.com/data_ocr.json?key=4523ab90&__method=POST')
  #pprint.pprint(r.json()) # This will convert our API data into JSON format and print it in a organized manner
  # loads method of json module is used to parse a valid string and convert it to Python dictionary
  data= json.loads(r.text)
  #dumps method of json module converts our json object into string and is further used for parsing,printing .
  data= json.dumps(data)
  #
  Dict= eval(data)
  #print(Dict)
  #print( Dict.get("id"))
  #print( Dict.get("first_name"))

  #print(Dict.get("last_name"))
  #print( Dict.get("datetime"))
  #print( Dict.get("gender"))
  #print( Dict.get("phone"))
  #print( Dict.get("make"))
  #print( Dict.get("model"))
  #print( Dict.get("model_yr"))
  #print( Dict.get("street_address"))
  #print( Dict.get("city"))
  #print( Dict.get("pincode"))
  # print( Dict.get("state"))


  # for x in Dict:
  #     FIRST_NAME=(x['first_name'])
  #     LAST_NAME=(x['last_name'])
  #     ID=(x['id'])
  #     print(FIRST_NAME)
  #     print(LAST_NAME)
  #     print(ID)



  #print(data)

  #print(type(Dict))
  # converting our Dictionary object to text file for recent records
  out_file = open("Data\\Recent.txt", "w")

  json.dump(Dict, out_file, indent=6)

  out_file.close()
  # converting our Dictionary object to text file  to store records from our API
  out_file1 = open("Data\\History.txt", "a")

  json.dump(Dict, out_file1, indent=6)

  out_file1.close()








  # window
  tkWindow = Tk()
  tkWindow.geometry('600x500')
  tkWindow.title('CUSTOMER _ INFORMATION')

  # username label and text entry box
  IDLabel = Label(tkWindow, text="REG. ID : ").grid(row=0, column=0)
  IDSLabel = Label(tkWindow, text=random.randint(1273547,9864821) +Dict.get("id")) .grid(row=0, column=1)


  # password label and password entry box
  FIRSTNAMELabel = Label(tkWindow, text="FIRST NAME: ").grid(row=1, column=0)
  FIRSTNAMELabel1 = Label(tkWindow, text=Dict.get("first_name")).grid(row=1, column=1)


  LASTNAMELabel = Label(tkWindow, text=Dict.get("last_name")).grid(row=2, column=1)
  LASTNAMESLabel = Label(tkWindow, text="LAST NAME: ").grid(row=2, column=0)

  DATELabel = Label(tkWindow, text=Dict.get("datetime")).grid(row=3, column=1)
  TIMELabel = Label(tkWindow, text="REG. DATE : ").grid(row=3, column=0)

  GENDERLabel = Label(tkWindow, text=Dict.get("gender")).grid(row=4, column=1)
  GENDERSLabel = Label(tkWindow, text="GENDER : ").grid(row=4, column=0)

  PHONELabel = Label(tkWindow, text=Dict.get("phone")).grid(row=5, column=1)
  IPHONELabel = Label(tkWindow, text="PHONE : ").grid(row=5, column=0)

  MAKELabel = Label(tkWindow, text=Dict.get("make")).grid(row=6, column=1)
  MAKERLabel = Label(tkWindow, text="MANUFATURER : ").grid(row=6, column=0)

  MODELLabel = Label(tkWindow, text=Dict.get("model")).grid(row=7, column=1)
  MODELSLabel = Label(tkWindow, text="MODEL : ").grid(row=7, column=0)

  MODELYEARLabel = Label(tkWindow, text=Dict.get("model_yr")).grid(row=8, column=1)
  YEARLabel = Label(tkWindow, text="MODEL YEAR : ").grid(row=8, column=0)

  STRRETADRESSLabel = Label(tkWindow, text=Dict.get("street_address")).grid(row=9, column=1)
  ADDRESSLabel = Label(tkWindow, text="STREET ADDRESS : ").grid(row=9, column=0)

  CITYLabel = Label(tkWindow, text=Dict.get("city")).grid(row=10, column=1)
  citLabel = Label(tkWindow, text="CITY : ").grid(row=10, column=0)

  PINLabel = Label(tkWindow, text=Dict.get("pincode")).grid(row=11, column=1)
  CODELabel = Label(tkWindow, text="PINCODE : ").grid(row=11, column=0)

  usernameLabel = Label(tkWindow, text=Dict.get("state")).grid(row=12, column=1)
  passwordLabel = Label(tkWindow, text="STATE : ").grid(row=12, column=0)
  # but2 = Button(text="Exit", command=tkWindow.destroy() ).grid(row =14,column=1)

  numberlabel= Label(tkWindow,text = str(num)).grid(row =13,column =1)
  numberlabel1 =Label(tkWindow,text= "Vehicle number").grid(row =13,column =0)

  tkWindow.mainloop()
  return




#NOTE: Dict.get method is used to call our API field objects stored in our dictionary




