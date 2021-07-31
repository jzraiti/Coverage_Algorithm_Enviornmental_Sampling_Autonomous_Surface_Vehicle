import numpy as np
import cv2 

# import sys
# sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from erosion_dilation import * 

from jasons_skeletonize import * 

from trim_edges import * # new_array = trim_edges(path,weight_threshold)

from skeleton_to_graph import * # graph = skeleton_to_graph(path)

from open_or_show_image import * # image = open_image(path) , show_image(image)




def inverse_skeletonize(path, weight_threshold):
    """takes in path to image and weight threshold to trim from 
        
    :param path: path to image
    :type path: string
    :param weight_threshold: number of pix to 
    :type option: int
    :param num: number of erosions and dilations respectively 
    :type num: int
    
    :rtype: integer np array of image , name of image that was written to file
    :return: image array and the name of the image file for finding it later 
    """
    
    # -------------- get background of correct size
    image = open_image(path) #numpy.ndarray (403,341) ->  (y,x) each y,x point has a value 225 or 0 
    black_image = np.zeros((image.shape[0],image.shape[1])) # get black background 
    white_image = black_image +255 #convert to white 

    # ---------------- get trimmed skeleton 
    # weight_threshold = 30
    new_array, new_image = trim_edges( path,weight_threshold ) # NEW ARRAY IS IN Y,X format, as a nested list of graph[edges[x,ypos]]


    for edge in new_array:
        for point in edge:
            white_image[point[0]][point[1]] = 0
            
    # show_image(white_image) # this is the inverse of thinned skel

    cv2.imwrite('negative_skeleton.png', white_image)
    #--------------------------------------------------- do erosion and dilation

    # path to image
    path = r'negative_skeleton.png'
    option = 1 
    num_erosions = 1
    num_dilations = 0

    # inputs = path to image, erode first (1) or dialate first (2) .desired number of erosions, desired number of dialations 
    # outputs = eroded then dialated image
    e_d_image , name = erosion_dilation(path,option,num_erosions,num_dilations)

    #-------------------------------------------------- get thinnned skel of skel
    #output spits out many images saved to same enviornment (skeleton, lee, medial axis, thinned, partial thinned)
    med_axis , skeleton , skeleton_lee , thinned , thinned_partial, name , paths_list = jasons_skeletonize(name)
    
    return med_axis , skeleton , skeleton_lee , thinned , thinned_partial, name , paths_list

