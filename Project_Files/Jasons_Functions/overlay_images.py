
import numpy as np
import cv2

# import sys
# sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from open_or_show_image import *
from get_negative_image import *
    
def overlay_images (image1,image2,make_negative_1, make_negative_2):
    """overlays two images with option to make either negative : note only works with making images with a white background
    
    :param path1 and 2: image array
    :type path1 and 2: int
    :param make_negative_1 and 2: make respective image negative (to have white background)
    :type make_negative_1 and 2: bool
    
    :rtype: integer numpy array
    :return:  white background black foreground image composite
    """

    #error check
    if image1.shape != image2.shape:
        print("ERROR: images are not of the same shape")
        
    #make negative 
    if make_negative_1:
        image1 = get_negative_image(image1)
    if make_negative_2:
        image2 = get_negative_image(image2)

    #make new image 
    white_image = np.ones((image1.shape[0],image1.shape[1])) # get black background 

    for i in range(0,image1.shape[0]):
        for j in range(0, image1.shape[1]):
            if image1[i][j] == 0 or image2[i][j]== 0:
                white_image[i][j] = 0
                
    new_image = white_image
    
    return new_image