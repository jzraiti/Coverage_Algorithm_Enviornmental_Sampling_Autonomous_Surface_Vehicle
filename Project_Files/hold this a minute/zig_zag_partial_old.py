

from re import search
from threading import local
import cv2
import numpy as np

import sys

from numpy.lib.function_base import diff
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from drawline import * 
from skeleton_to_graph import * # graph = skeleton_to_graph(path)
from open_or_show_image import *
from find_line_segment_intersection import *
from matplotlib.path import Path

def get_negative_image(image):
    image = (255 - image)
    return image

# def find_nearest_white(img, target):
#     nonzero = cv2.findNonZero(img)
#     distances = np.sqrt((nonzero[:,:,0] - target[0]) ** 2 + (nonzero[:,:,1] - target[1]) ** 2) 
#     # distances = np.sqrt((nonzero[:,:,0] - target[1]) ** 2 + (nonzero[:,:,1] - target[0]) ** 2) # try flipping the coordinates 
#     nearest_index = np.argmin(distances)
#     return nonzero[nearest_index]



def find_nearest_white(img, target):
    nonzero = np.argwhere(img == 255)
    distances = np.sqrt((nonzero[:,0] - target[0]) ** 2 + (nonzero[:,1] - target[1]) ** 2)
    nearest_index = np.argmin(distances)
    return nonzero[nearest_index]



def zig_zag_partial(start_point,end_point,boundary_image, new_image, i ): #zigzagsize will scale the size of the zig zags
    #inputs: start_point,end_point,zig_zag_image,boundary_image, i
    #   i is just an integer, if even it will zig, if odd it will zag

    
    slope_vector = np.array([  end_point[0]- start_point[0] , end_point[1] - start_point[1] ]) # vector representation of slope here in format [y , x]
    # step_vector = slope_vector / (num_turns - 1) # partition total change inslope into steps to zig zag across and -1 because the number of turns will be one less than the number of partitions (also in format [y , x])
    
    
    
    normalized_slope_vector = slope_vector/np.linalg.norm(slope_vector) # here we are getting the normalized step_vector so we can use its direction and ignore its magnitude 
    # print(normalized_slope_vector)
    
    #--------------------- find closest obstactle in perpendicular polygon (boundary is start and end points and the 2 perpendicular image edge points )
    #--------- get vector (in correct direction) perpendicular slope to calculate distance to nearest boundary in path of zig zag
    if i%2 ==0: # set zig and zag values (with alternating directions): this is basically creating zig zag vector perpendicular to the skeleton chunk input
        normalized_perpendicular_vector  = [-normalized_slope_vector[1], normalized_slope_vector[0]]
    else:
        normalized_perpendicular_vector  = [normalized_slope_vector[1], -normalized_slope_vector[0]]
    #------------- find corresponding edge points
    
    scalar = boundary_image.shape[0]+boundary_image.shape[1]
    out_of_bounds_scalar = np.multiply(normalized_perpendicular_vector, scalar) # this is to guarantee the start /endpoint linesegments extend past edges of images 
    


    #define bounds of image
    #try with actual bounds of image (there may be edge cases where this does not work)
    top_side    = [(0,0) , (0,boundary_image.shape[1] )]
    bottom_side = [(boundary_image.shape[0] ,boundary_image.shape[1] ) , (boundary_image.shape[0] ,0) ]
    right_side  = [(0 ,boundary_image.shape[1] ) , (boundary_image.shape[0] ,boundary_image.shape[1])]
    left_side   = [(boundary_image.shape[0],0) , (0,0)]
    # top_side    = [(1,1) , (1,boundary_image.shape[1] -1 )]
    # bottom_side = [(boundary_image.shape[0] -1,boundary_image.shape[1] -1) , (boundary_image.shape[0]-1 ,1) ]
    # right_side  = [(1 ,boundary_image.shape[1] - 1) , (boundary_image.shape[0]-1,boundary_image.shape[1]-1)]
    # left_side   = [(boundary_image.shape[0]-1,1) , (1,1)]
    
    
    #define perpendiculat start and endpoint lines 
    start_point_perpendicular_line = [ start_point, start_point + out_of_bounds_scalar ]
    end_point_perpendicular_line   = [ end_point, end_point + out_of_bounds_scalar ]
    
    #create for loop for finding corresponding edge intersection
    sides_list = [ top_side, bottom_side, right_side, left_side]
    
    # # TEST 
    # search_zone = np.zeros((boundary_image.shape[0],boundary_image.shape[1])) # get black background 
    
    # for side in sides_list:
    #     search_zone = drawline(np.array(side[0]),np.array(side[1]),search_zone)
    # search_zone= drawline(np.array(start_point_perpendicular_line[0]),np.array(start_point_perpendicular_line[1]), search_zone )
    # # show_image(search_zone)
    
    
    for side in sides_list:
        try:    start_point_intersection = find_line_segment_intersection(start_point_perpendicular_line,side)
        except: pass
        try:    end_point_intersection   = find_line_segment_intersection(end_point_perpendicular_line,side)
        except: pass
    print(start_point_intersection,end_point_intersection)

    # ------------- create polygon of search area for find nearest white

    tupVerts=[ start_point, end_point , end_point_intersection,start_point_intersection ] #verticies of polygon search area

    dim1 = boundary_image.shape[0]
    dim2 = boundary_image.shape[1]
    if dim1 >= dim2: grid_dim = dim1 # this is just to accommodate how i am making the polygon area, i know its werid
    else: grid_dim = dim2
    
    x, y = np.meshgrid(np.arange(grid_dim), np.arange(grid_dim)) # make a canvas with coordinates
    x, y = x.flatten(), y.flatten()
    points = np.vstack((x,y)).T #changed x, y to y,x 

    p = Path(tupVerts) # make a polygon
    # show_image(p)
    grid = p.contains_points(points)
    mask = grid.reshape(grid_dim,-grid_dim) # now you have a mask with points inside a polygon
    # show_image(mask)
    #-----------fix mask shape and switch mask x and y values
    mask = np.swapaxes(mask,0,1)
    
    difference = abs(dim1 - dim2)
    if difference > 0:
        for d in range(1,difference+1):
            if dim1 > dim2:
                #delete extra dimensions
                mask = np.delete(mask,-1,1)
            elif dim2 > dim1:
                #delete extra dimensions
                mask = np.delete(mask,-1,0)
    # show_image(mask)
    #check mask is of proper size
    # print("mask if of shape: ", mask.shape , " original dimensions are:", dim1,dim2)
    
    #------------------------ combine information from boundary image with search zone of mask
    negative_image = get_negative_image( boundary_image)
    # show_image(negative_image)
    
    mask = mask *255 #convert mask to integer array
    
    search_zone = np.zeros((boundary_image.shape[0],boundary_image.shape[1])) # get black background 
    for col in range(0,dim1):
        for row in range(0,dim2):
            if negative_image[col][row] > 0 and negative_image[col][row] == mask[col][row]:
                search_zone[col][row] = 255

    # show_image(search_zone)

    # ----------------- find nearest white image! 
    a = find_nearest_white( search_zone, end_point) #find nearest object in search zone  
    b = end_point
    
    dist = np.linalg.norm(a-b) #this calculates euclidean distance between two points 
    # print("distance from nearest boundary ", dist , '\n')
    zig_zag_size_vector = normalized_slope_vector * int(dist-.05) # make the zig zag only as far as the closest boundary 

    if dist == 0: 
        # show_image ( negative_image)
        print("warning: point at ", b , "distance from nearest boundary is ", dist , '\n')
    # print(zig_zag_size_vector)

    # ----------------------- below the actual zig zags happen 

    if i%2 ==0: # set zig and zag values (with alternating directions): this is basically creating zig zag vector perpendicular to the skeleton chunk input
        zigzag = [-zig_zag_size_vector[1], zig_zag_size_vector[0]]
    else:
        zigzag = [zig_zag_size_vector[1], -zig_zag_size_vector[0]]

    pt1 = start_point
    pt2 = end_point + zigzag
    pt3 = end_point
    # try : zig_zag_image = drawline(pt1,pt2,zig_zag_image)
    # except : print("error zigging")
    # try : zig_zag_image = drawline(pt2,pt3,zig_zag_image)
    # except : print("error zigging")
    
    try : zig_zag_image = drawline(pt1,pt2,new_image)
    except : print("error zigging")
    try : zig_zag_image = drawline(pt2,pt3,new_image)
    except : print("error zigging")
    
    #image = drawline(start_point,end_point,image) #this is just for error checking, draw a line between start and end points 
    #show_image(image)
    # show_image(get_negative_image( boundary_image))
    return(new_image)



# future me : this is what happens --> make array of all pixels on perpedicular vector 
# make 1 directional --> only in direction of zig zag