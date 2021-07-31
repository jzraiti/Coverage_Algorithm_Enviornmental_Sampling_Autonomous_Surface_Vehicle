# importing cv2
import cv2

# importing numpy
import numpy as np

# plotting
import matplotlib.pyplot as plt

# import sys
# sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from open_or_show_image import * 

# inputs = path to image, erode first (1) or dialate first (2) .desired number of erosions, desired number of dialations 
# outputs = eroded then dialated image

def erosion_dilation(path,option,num_erosions,num_dilations):
    """takes in two np array points and an image to draw on, spits out the image with a line between points 
        
    :param path: path to image
    :type path: string
    :param option: 1=dialate first or 2=erode first  
    :type option: int
    :param num: number of erosions and dilations respectively 
    :type num: int
    
    :rtype: integer np array of image , name of image that was written to file
    :return: image array and the name of the image file for finding it later 
    """
    # Reading an image in default mode
    image = open_image(path)
    
    # Creating kernel
    kernel = np.ones((3, 3), np.uint8)
    if option == 1 :
        e_d_image = image
        e_d_image = cv2.erode( e_d_image, kernel, iterations=num_erosions ) 
        e_d_image = cv2.dilate( e_d_image, kernel, iterations=num_dilations ) 
    elif option == 2 : 
        try:
            e_d_image = image
            e_d_image = cv2.erode( e_d_image, kernel, iterations=num_erosions ) 
            e_d_image = cv2.dilate( e_d_image, kernel, iterations=num_dilations ) 
        except:
            print("dilation/erosion failed")
    
    if option == 1:
        name = 'e' + str(num_erosions) + r'_d' + str(num_dilations) 
    elif option == 2:
        name =  r'_d' + str(num_dilations) +  'e' + str(num_erosions)
    else:
        print('error: invalid option')
    
    name = name + '_' + str(path)
    name = name.replace("/", "_")
    name = name.replace(".", "_")
    name = str(name) + '.png' 
    
    cv2.imwrite(name, e_d_image )
    
    return[ e_d_image , name]

