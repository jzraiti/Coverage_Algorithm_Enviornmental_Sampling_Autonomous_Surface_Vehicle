import cv2 
import numpy as np

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from zig_zag_partial import * #inputs: start_point,end_point,zig_zag_size,zig_zag_image,boundary_image, i
from skeleton_to_graph import * 

def zig_zag_full_image ( path_to_skeleton, path_to_boundary_image, zig_zag_width):
    """makes a full zig zag image ready to be used for traveling salesman solution and then conversion to coordinate points/mission plan
    
    :param path_to_skeleton: full path to a preprocessed skeleton
    :type path_to_skeleton: str
    :param path_to_boundary_image: full path to preprocessed boundaries image
    :type path_to_boundary_image: str
    :param: desired zig_zag_width (in pixels)
    :type: int
    
    :rtype: integer numpy array
    :return:  a black background white forground image of just the zig zag path (full)
    """
    #start by converting skel to graph and boundary image 
    graph = skeleton_to_graph(path_to_skeleton)
    boundary_image = open_image(path_to_boundary_image)

    #create new image to be return value 
    new_image = np.zeros((boundary_image.shape[0],boundary_image.shape[1])) # get black background 
    
    for (s,e) in graph.edges():
        #get points on skeleton edge and number of points per edge
        points = graph[s][e]['pts']
        num_points = len(points)
        
        #partition chunks for zig zagging
        x = int( (num_points - num_points%zig_zag_width) /zig_zag_width ) # this is to prevent the chunks of the line going past the endpoint
        
        #call actual zig_zag function
        for i in range(0 , x-1 ):     #   i is just an integer, if even it will zig, if odd it will zag
            start_point = np.array([ points[ i  * zig_zag_width  ][0] , points[ i * zig_zag_width  ][1] ])
            end_point   = np.array([ points[ (i+1) * zig_zag_width ][0] , points[ (i+1) * zig_zag_width  ][1] ])

            image = zig_zag_partial(  start_point  ,  end_point  , boundary_image , new_image , i)
    
    return image
