import cv2 
import numpy as np

# import sys
# sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from zig_zag_partial_3 import * #inputs: start_point,end_point,zig_zag_size,zig_zag_image,boundary_image, i
from skeleton_to_graph import * 
from drawline import * 

def zig_zag_full_image_3 ( path_to_skeleton, path_to_boundary_image, zig_zag_width ):
    """makes a full zig zag image ready to be used for traveling salesman solution and then conversion to coordinate points/mission plan
    
    :param path_to_skeleton: full path to a preprocessed skeleton
    :type path_to_skeleton: str
    :param path_to_boundary_image: full path to preprocessed boundaries image
    :type path_to_boundary_image: str
    :param: desired zig_zag_width (in pixels)
    :type: int
    
    :rtype: integer numpy array , dict { (tuple coord y,x) : [points] }
    :return:  a black background white forground image of just the zig zag path (full) and dictionary of edges and points 
    """
    #start by converting skel to graph and boundary image 
    graph = skeleton_to_graph(path_to_skeleton)
    boundary_image = open_image(path_to_boundary_image)

    #create new image to be return value 
    new_image = np.zeros((boundary_image.shape[0],boundary_image.shape[1])) # get black background 
    
    zig_zag_threshold = int(zig_zag_width) #basically if the distance to an obstacle is less than the width of a zig zag dont bother doing it

    new_boundary_image = boundary_image # this is going to be the boundary image updated with already draw edges 
    
    # need to create a dict that contains [node1,node2] = [pts] and [node2,node1] = [pts backwards]
    zig_zag_points_dict = {} #the array that will contain the points on the line
    
    for (s,e) in graph.edges():
        all_points_on_line_array = [] #stores all the points on a line s,e
        #get points on skeleton edge and number of points per edge
        points = graph[s][e]['pts']
        num_points = len(points)
        
        #partition chunks for zig zagging
        x = int( (num_points - num_points%zig_zag_width) /zig_zag_width ) # this is to prevent the chunks of the line going past the endpoint
        remainder_pixels = num_points%zig_zag_width
        
        #call actual zig_zag function
        for i in range(0 , x ):     #   i is just an integer, if even it will zig, if odd it will zag (x-1 because index at zero)
            if i == x-1: #make last zig zag go all the way to the end point #hopefully this will create a continuous graph
                start_point = np.array([ points[ i  * zig_zag_width  ][0] , points[ i * zig_zag_width   ][1] ])
                end_point   = np.array([ points[ (i+1) * zig_zag_width +remainder_pixels -1 ][0] , points[ (i+1) * zig_zag_width +remainder_pixels -1 ][1] ]) # - 1 here to keep things in bounds 
            else: 
                start_point = np.array([ points[ i  * zig_zag_width  ][0] , points[ i * zig_zag_width  ][1] ])
                end_point   = np.array([ points[ (i+1) * zig_zag_width ][0] , points[ (i+1) * zig_zag_width  ][1] ])

            # new_image = drawline(start_point,end_point,new_image) # draws line between beginning and ending
            image, new_boundary_image, line_array = zig_zag_partial_3(  start_point  ,  end_point  , new_boundary_image , new_image , i , zig_zag_threshold)
            # show_image(new_boundary_image)
            # show_image(image)
            all_points_on_line_array.extend(line_array)
        
        zig_zag_points_dict[(s,e)] =  all_points_on_line_array #add (node1,node2) : pts  to dict
        # print(all_points_on_line_array[0])
        # if len(all_points_on_line_array):
        #     print("this is good")
        # else:
        #     print("this is not good ")
        all_points_on_line_array.reverse()
        zig_zag_points_dict[(e,s)] =  all_points_on_line_array #add (node2,node1) : pts.reverse()  to dict
        # print(all_points_on_line_array[0])
        # if len(all_points_on_line_array):
        #     print("this is good")
        # else:
        #     print("this is not good ")
    return image, zig_zag_points_dict
