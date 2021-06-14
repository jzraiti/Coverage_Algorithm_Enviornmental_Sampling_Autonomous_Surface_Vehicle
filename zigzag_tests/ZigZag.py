# importing cv2
import cv2

#import matplotlib for plotting since cv2 doesnt seem to want to do that
import matplotlib.pyplot as plt

import numpy as np
import math

def slope1(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def slope2(point1, point2):
    return (point2[1]-point1[1])/(point2[0]-point1[0])

def distance2(p1, p2):
    return( math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ) )

def drawline(p1,p2,image):
    # Start coordinate, here (225, 0) tuple
    # represents the top right corner of image

    start_point = tuple(p1.astype(int).tolist()) #input is numpyfloat array
    end_point = tuple(p2.astype(int).tolist()) # cv2.line needs tuple int inputs 

    # Black color in BGR
    color = (0, 0, 0)
    # Line thickness of 1 px
    thickness = 1
    # Using cv2.line() method
    # Draw a diagonal black line with thickness of 1 px
    image = cv2.line(image, start_point, end_point, color, thickness) #######------
    return(image)

def open_image():
        #fun fact r represents raw string so that backslashes are left in
    image_path = r'/home/jasonraiti/Documents/GitHub/USC_REU/OpenCV_tests/test.png'
    path = image_path
    # Reading an image in grayscale mode
    image = cv2.imread(path, 0)

    if image is None:
        print("Check file path")
    return(image)

def show_image(image):
    #plot with matplt.lib instead
    plt.imshow(image)
    plt.show()
    print("Plotted")

def zigzag(start_point,end_point,num_turns):
    
    #start by opening the image, choose image in the function 
    image = open_image()
    
    
    #num turns must be greater than 1 
    slope_vector = np.array([ end_point[1] - start_point[1], end_point[0]- start_point[0] ])
    step_vector = slope_vector / (num_turns - 1) # because the number of turns will be one less than the number of partitions
    for i in range(0,num_turns): 
        #connect point i and point i+1
        
        pt1 = start_point + step_vector*(i)
        pt2 = start_point + step_vector*(i+1)

        if i%2 ==0:
            zigzag = step_vector * np.array([-1,1])
        else:
            zigzag = step_vector * np.array([1,-1])
        
        #if i is start point
        if i == 0:
            pt1 = start_point + step_vector*(i)
            pt2 = start_point + step_vector*(i+1) + zigzag
            
            image = drawline(pt1,pt2,image)

            pt_old = pt2 #save endpoint
        #elif i+1 is endpoint
        elif i == num_turns-1:
            pt1 = pt_old
            pt2 = start_point + step_vector*(i+1) 
            #if i%2==0:
            #    pt2 = pt2* np.array([ -1,1])

            image = drawline(pt1,pt2,image)
        
        else: #otherwise in the middle 
            pt1 = pt_old
            pt2 = start_point + step_vector*(i+1) +zigzag
            image = drawline(pt1,pt2,image)

            pt_old =pt2 #save endpoint for next start 

    show_image(image)

#note that 0,0 is top left corner and 225,225 is bottom right
start_point = np.array([ 10 , 20]) #list[] vs tuple() coordinates
end_point = np.array([130,140])

zigzag(start_point,end_point,3)

