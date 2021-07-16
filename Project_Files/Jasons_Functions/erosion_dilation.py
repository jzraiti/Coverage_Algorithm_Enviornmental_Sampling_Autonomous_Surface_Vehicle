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

def erosion_dilation(path,option,num_erosions,num_dilations):
    # Reading an image in default mode
    image = open_image(path)
    
    # image = image > 123 # filter out any in between values
        
    
    # Creating kernel
    kernel = np.ones((3, 3), np.uint8)
    if option == 1 :
        # try:
        #     e_d_image = image
        #     e_d_image = cv2.erode( e_d_image, kernel, iterations=num_erosions ) 
        #     e_d_image = cv2.dilate( e_d_image, kernel, iterations=num_dilations ) 
        # except:
        #     print("erosion/dilation failed")
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
    # show_image(e_d_image)
    # cv2.imwrite('e{}_d{}_{}.png'.format(num_erosions,num_dilations,path), e_d_image )
    # cv2.imwrite('e_d_image.png', e_d_image )
    
    if option == 1:
        name = 'e' + str(num_erosions) + r'_d' + str(num_dilations) 
    elif option == 2:
        name =  + r'_d' + str(num_dilations) +  'e' + str(num_erosions)
    else:
        print('error: invalid option')
        
        #create name for files
    # print(path)
    name = name + '_' + str(path)
    name = name.replace("/", "_")
    name = name.replace(".", "_")
    name = str(name) + '.png' 
    cv2.imwrite(name, e_d_image )
    
    return[ e_d_image , name]



# # path to image
# path = r'./skeletonize_skeleton/negative_skeleton.png'
# option = 1 
# num_erosions = 1
# num_dilations = 0

# erosion_dilation(path,option,num_erosions,num_dilations)