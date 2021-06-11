# importing cv2
import cv2

#import matplotlib for plotting since cv2 doesnt seem to want to do that
import matplotlib.pyplot as plt

import numpy as np
import math


def zigzag(start_point,end_point,num_segments):
    #slope1(start_point[0],start_point[1],end_point[0],end_point[1])
    m = slope2(start_point, end_point)

def slope1(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def slope2(point1, point2):
    return (point2[1]-point1[1])/(point2[0]-point1[0])

def distance2(p1, p2):
    return( math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ) )

def drawline(p1,p2):
    #fun fact r represents raw string so that backslashes are left in
    image_path = r'/home/jasonraiti/Documents/GitHub/USC_REU/OpenCV_tests/test.png'
    path = image_path
    # Reading an image in grayscale mode
    image = cv2.imread(path, 0)

    if image is None:
        print("Check file path")
    # Window name in which image is displayed
    window_name = 'Image'
    # Start coordinate, here (225, 0) tuple
    # represents the top right corner of image
    start_point = (0, 100)
    end_point = (225, 225)
    # Black color in BGR
    color = (0, 0, 0)
    # Line thickness of 1 px
    thickness = 1
    # Using cv2.line() method
    # Draw a diagonal black line with thickness of 1 px
    image = cv2.line(image, start_point, end_point, color, thickness)
    # Displaying the image
    #cv2.imshow(window_name, image) THIS SHIT DONT WORK 

    #plot with matplt.lib instead
    plt.imshow(image, cmap='gray')
    plt.show()

    print("done")

start_point = np.array([ 0 , 0]) #list[] vs tuple() coordinates
end_point = np.array([100,100])

drawline(start_point,end_point)