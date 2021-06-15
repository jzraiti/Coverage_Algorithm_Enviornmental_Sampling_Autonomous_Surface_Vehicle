import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#find lake image file
img = cv.imread(cv.samples.findFile("Lake_Murray_Map/SouthEastCorner_BW.jpg"),0)

#img = cv.imread('gradient.png',0)

#try different thresholding techniques 
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY) #I think this is the one we want
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

#plot for comparison
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv.imwrite("SouthEastCorner_BW.png", thresh1)

