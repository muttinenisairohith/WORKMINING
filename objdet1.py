import Tkinter
import tkMessageBox
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
#import test
#from test import *
#cap = cv2.VideoCapture(0)

#while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()

img = cv2.imread('img7.jpg',1)
rgb = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
hsv =cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([20,100,150])
upper_yellow = np.array([100,255,255])

mask=cv2.inRange(hsv, lower_yellow, upper_yellow)
res= cv2.bitwise_and(rgb,rgb,mask = mask)


plt.imshow(res)
plt.show()
#cv2.imwrite("res.jpg",res)
#plt.imshow(mask)
#plt.show()
#plt.imshow(hsv)
#plt.show()
#plt.imshow(rgb)
#plt.show()
cv2.destroyAllWindows()
count=0
"""count=0
for i in range(0,178):
	for j in range(0,255):
		if mask[i,j]==255:
			count=count+1
print count
"""

#if count>200:
#	os.system('detect.py')

if count==0:
   tkMessageBox.showinfo("error","error")
if count==10:
   tkMessageBox.showinfo("no error","no error")


