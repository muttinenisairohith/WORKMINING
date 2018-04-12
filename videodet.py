import tkinter
#import tkMessageBox
from tkinter import messagebox
import cv2
import os
import urllib

import numpy as np
from matplotlib import pyplot as plt
#import test
#from test import *
url='http://192.168.0.5:8080/shot.jpg'

while(True):
    #Capture frame-by-frame
        imgResp = urllib.request.urlopen(url)
    
    # Numpy to convert into a array
        imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
    # Finally decode the array to OpenCV usable format ;) 
        img = cv2.imdecode(imgNp,-1)
        rgb = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        hsv =cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([20,100,150])
        upper_yellow = np.array([100,255,255])

        mask=cv2.inRange(hsv, lower_yellow, upper_yellow)
        res= cv2.bitwise_and(rgb,rgb,mask = mask)

        cv2.imshow('rgb',img)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        cv2.waitKey(1)
        #cv2.imwrite("res.jpg",res)
#plt.imshow(mask)
#plt.show()
#plt.imshow(hsv)
#plt.show()
#plt.imshow(rgb)
#plt.show()
        count=0
        for i in range(0,178):
                for j in range(0,255):
                    if mask[i,j]==255:
                        count=count+1
        if count>200:
                break
#if count>200:
#	os.system('detect.py')

if count>200:
   messagebox.showinfo("error","error")
if count<200:
   messagebox.showinfo("no error","no error")


