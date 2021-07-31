# importing cv2
import cv2

# importing numpy
import numpy as np

# plotting
import matplotlib.pyplot as plt

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from open_or_show_image import * 

# inputs = path to image, erode first (1) or dialate first (2) .desired number of erosions, desired number of dialations 
# outputs = eroded then dialated image

def erosion_dilation_from_array(image,option,num_erosions,num_dilations):
    """takes in two np array points and an image to draw on, spits out the image with a line between points 
        
    :param image: image array of thing you want eroded np.uint8 / dialated
    :type image: np.uint8 array
    :param option: 1=dialate first or 2=erode first  
    :type option: int
    :param num: number of erosions and dilations respectively 
    :type num: int
    
    :rtype: integer np array of image 
    :return: image array and the name 
    """
    # Note : " needs data type:  np.uint8"
    e_d_image = image 
    # Creating kernel
    kernel = np.ones((3, 3), np.uint8) 
    if option == 1 : 
        e_d_image = cv2.erode( e_d_image, kernel, iterations=num_erosions ) 
        e_d_image = cv2.dilate( e_d_image, kernel, iterations=num_dilations ) 
    elif option == 2 : 
        try:
            e_d_image = cv2.erode( e_d_image, kernel, iterations=num_erosions ) 
            e_d_image = cv2.dilate( e_d_image, kernel, iterations=num_dilations ) 
        except:
            print("dilation/erosion failed")
    else:
        print('error: invalid option')
    
    return e_d_image

