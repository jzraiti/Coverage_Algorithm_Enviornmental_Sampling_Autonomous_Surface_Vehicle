import numpy as np
import cv2 

# import sys
# sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from erosion_dilation_from_array import * 

from jasons_skeletonize_from_array import * 

from trim_edges import * # new_array = trim_edges(path,weight_threshold)

from skeleton_to_graph import * # graph = skeleton_to_graph(path)

from open_or_show_image import * # image = open_image(path) , show_image(image)

from get_negative_image import *



def inverse_skeletonize_from_array(image):
    """takes old skeleton image
        
    :param image:  original skeleton image
    :type image: int np array
    
    :rtype: integer np array of images , list of paths to each skeleton
    :return: image arrays of each inverse skeleton and the path to each corresponding image file
    """
    
    negative_image = get_negative_image(image)

    # cv2.imwrite('negative_skeleton.png', negative_image)
    #--------------------------------------------------- do erosion and dilation

    # path to image
    # path = r'negative_skeleton.png'
    option = 1 
    num_erosions = 1 
    num_dilations = 0

    e_d_image = erosion_dilation_from_array(negative_image,option,num_erosions,num_dilations)
    # print("from inverse_skeletonize_from_array: eroded the negative image" , num_erosions)
    # show_image(e_d_image)
    #-------------------------------------------------- get thinnned skel of skel
    med_axis , skeleton , skeleton_lee , thinned , thinned_partial = jasons_skeletonize_from_array(e_d_image)
    
    return med_axis , skeleton , skeleton_lee , thinned , thinned_partial

