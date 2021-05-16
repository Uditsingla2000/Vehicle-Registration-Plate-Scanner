import cv2     #image processing external library 
#pip install opencv
import imutils  #to resize image
#import install imutils
import pytesseract  #Google OCR library
# pip install pytessaecact


from tkinter import *

# os.remove('1.png')
# newf=r'C:\Users\hp\Desktop\python practice\3.jpg'
def newfunction(arg):
    global filename
    filename=arg
    newf=filename
    print(filename)

    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    #accessing the tesserect.exe file for OCR by putting the address of file here

    #now for accessing and reading image file
    image = cv2.imread(newf,cv2.IMREAD_UNCHANGED)
    # try code on -> plate1,plate6,plate10,plate12 

    #resize and standardise the image to 500px
    image = imutils.resize(image, width= 500)

    #Display original image when it starts finding
    # cv2.imshow("Original Image",image)  #here original image is name of window
    # cv2.waitKey(0)  #execution waits for response


    #Converting image to grayscale
    #it will reduce dimentions and complexity of image
    #image processing algorithms like "canny" etc only work in grayscale

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Grayscale image",gray)
    # cv2.waitKey(0)


    #now reducing noise from image and making it smooth
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    # cv2.imshow("Smoother image",gray)
    # cv2.waitKey(0)

    #so now we will find the edges of objects in image
    edged = cv2.Canny(gray, 170, 200)
    # cv2.imshow("Cany edge", edged)
    # cv2.waitKey(0)

    #now we will find contours based on the image
    cnts , new = cv2.findContours(edged.copy() , cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #here cnts is contour which means that it is like the curve joining all the contior points
    # new  is heirarchy relationship
    #RETR_list : it retrives all the contours but doesn't create any parent child relationship
    #CHAIN_APPROX_SIMPLE : IT REMOVES all the redundant points and complress the contour by saving memory


    #we will create a copy of our original image to draw all the contours
    image1 = image.copy()
    cv2.drawContours(image1, cnts, -1, (0,255,0), 3)
    #these parameters are fixed ## to draw all the contours in an
    # cv2.imshow("Canny after contouring ",image1)
    # cv2.waitKey(0)

    #but we dont want all the contours , we are intrested in only the number plate
    #we will select those area which are maximum so we will select top 30 areas
    #but it will give sorted is in order of min to maximum
    #so for that we will reverse the order of Sorting


    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
    NumberPlantCount= None

    #because currently we dont dont have any contour 
    #or you can say it eill show how many number plates are there in the image

    #to draw top 30 contours , we will make copy of original image and use
    # use it because we dont want to edit anything in our original image
    # 

    image2 =image.copy()
    cv2.drawContours(image2, cnts, -1, (0,255,0),3)
    # cv2.imshow("Filtering",image2)      # "filtering" -> "top 30 contours"
    # cv2.waitKey(0)


    #now we will run a for loop to find the best possible contour of our expected number plate

    count =0;
    name = 1    #name of the image (cropped image)

    for i in cnts:
        perimeter = cv2.arcLength(i, True)
        #perimeter is also called as arclength and we can find directly in python using arclength function

        approx =cv2.approxPolyDP(i, 0.02*perimeter, True)
        #approxPolyDP , we used it bcoz it approximates the curve of polygon with the precision
        if(len(approx) == 4):
            NumberPlantCount = approx
            #now we will crop that recatngle part of the number plate

            x, y, w, h = cv2.boundingRect(i)
            crp_img = image[y:y+h , x:x+w]

                #lets supose this is our figure with 4 corners

                    ###########################
                    #                         #
            #(y+h)  #                         #
                    #                         #
                    ###########################
            #(x+w)      -----(x+w)------->
                
                #it will crop this much part

            cv2.imwrite(str(name)+ '.png',crp_img)
            name += 1

            break

    #now we will draw contour in our main image that we have identified as a number plate
    cv2.drawContours(image,[NumberPlantCount], -1, (0,255,0),3)
    # cv2.imshow("Final Image", image)
    # cv2.waitKey(0)



    #we will crop only the part of number plate

    crop_img_loc = '1.png'
    # cv2.imshow("Cropped Image",cv2.imread(crop_img_loc))
    # cv2.waitKey(0)

    # # gaussian_blur_license_plate = cv2.GaussianBlur( crop_img_loc, (5, 5), 0) 
    # gaussian_blur_license_plate ='2.png'
    # gaussian_blur_license_plate = cv2.GaussianBlur(crop_img_loc, (5,5), 0) 
    # cv2.imshow("Denoised image",cv2.imread(gaussian_blur_license_plate))
    # cv2.waitKey(0)



    #extracting text from image


    text =pytesseract.image_to_string(crop_img_loc,lang='eng')
    if text=="":
        text="Error"
    print("Scanned text: ",text)
    print("--------------------------")
    #converting string to alphanumeric string(cintaining only numbers and alphabetes)
    alphanumeric =""
    for character in text:
        if character.isalnum():
            alphanumeric += character

    print("Number is : ",alphanumeric)
    print("--------------------------")
    print("\n")

    return alphanumeric
    # cv2.waitKey(0)


