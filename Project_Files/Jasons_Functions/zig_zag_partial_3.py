import numpy as np
from matplotlib.path import Path

# import sys

# sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from drawline import * 
from skeleton_to_graph import * # graph = skeleton_to_graph(path)
from open_or_show_image import *
from find_line_segment_intersection import *
from get_negative_image import *
from find_nearest_white import *

#from https://stackoverflow.com/questions/25837544/get-all-points-of-a-straight-line-in-python
def get_line(x1, y1, x2, y2):
    """
    Get all points along the line between pt1 x1,y1 and x2,y2
    """
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points

def zig_zag_partial_3(start_point,end_point,boundary_image, new_image, i , zig_zag_threshold ): #zigzagsize will scale the size of the zig zags
    """makes a zig zag on alternating sides between starting point and end point and avoiding boundaries marked in boundary image
    
    :param start_point: coordinates of starting point
    :type start_point: integer np array
    :param end_point: coordinates of ending point
    :type end_point: integer np array
    :param boundary_image: integer array of image demarkates boundaries of zig zags BLACK ON WHITE BACKGROUND
    :type boundary_image: integer array of image
    :param new_image: completely black integer array of image
    :type new_image: integer array of image
    :param i: determines direction of zig_zag, even or odd
    :type i: integer 
    
    :rtype: integer array of entire image , array of points on line (coord int) of zig zag
    :return: black image of one zig zag , overlay image + one zig zag, array of points added to zig zag 
    """
    
    dim1 = boundary_image.shape[0] # will use this dimension value sporadically sorry
    dim2 = boundary_image.shape[1]
    
    slope_vector = np.array([  end_point[0]- start_point[0] , end_point[1] - start_point[1] ]) # vector representation of slope here in format [y , x]
    normalized_slope_vector = slope_vector/np.linalg.norm(slope_vector) # here we are getting the normalized step_vector so we can use its direction and ignore its magnitude 
    
    #--------- get vector (in correct direction) perpendicular slope to calculate distance to nearest boundary in path of zig zag
    
    if i%2 ==0: # set zig and zag values (with alternating directions): this is basically creating zig zag vector perpendicular to the skeleton chunk input
        normalized_perpendicular_vector  = [-normalized_slope_vector[1], normalized_slope_vector[0]]
    else:
        normalized_perpendicular_vector  = [normalized_slope_vector[1], -normalized_slope_vector[0]]
    #------------- find corresponding edge points
    
    #this is to guantee intersection with a boundary
    scalar = boundary_image.shape[0]+boundary_image.shape[1]
    out_of_bounds_scalar = np.multiply(normalized_perpendicular_vector, scalar) # this is to guarantee the start /endpoint linesegments extend past edges of images 
    


    #define bounds of image, with actual bounds of image (there may be edge cases where this does not work)
    top_side    = [(0,0) , (0,boundary_image.shape[1] )]
    bottom_side = [(boundary_image.shape[0] ,boundary_image.shape[1] ) , (boundary_image.shape[0] ,0) ]
    right_side  = [(0 ,boundary_image.shape[1] ) , (boundary_image.shape[0] ,boundary_image.shape[1])]
    left_side   = [(boundary_image.shape[0],0) , (0,0)]
    
    #define perpendiculat start and endpoint lines 
    start_point_perpendicular_line = [ start_point, start_point + out_of_bounds_scalar ]
    end_point_perpendicular_line   = [ end_point, end_point + out_of_bounds_scalar ]
    
    #create for loop for finding corresponding edge intersection
    sides_list = [ top_side, bottom_side, right_side, left_side]
    
    for side in sides_list:
        try:    start_point_intersection = find_line_segment_intersection(start_point_perpendicular_line,side)
        except: pass
        try:    end_point_intersection   = find_line_segment_intersection(end_point_perpendicular_line,side)
        except: pass

    # ------------- create polygon of search area for find nearest white
    
    #verticies of polygon search area
    #add a cheeky nudge to the endpoint to make sure the last zig zag doesnt intrude too far
    tupVerts=[ start_point  + np.multiply(normalized_perpendicular_vector,2)
                , end_point  + np.multiply(normalized_perpendicular_vector,2)
                , end_point  + np.multiply(normalized_perpendicular_vector,4) + np.multiply(normalized_slope_vector , 4) # search area widened
                
                , end_point_intersection + np.multiply(normalized_slope_vector , 4) # search area widened
                , start_point_intersection - np.multiply(normalized_slope_vector , 4) #search area widened 
                , start_point + np.multiply(normalized_perpendicular_vector,4) - np.multiply(normalized_slope_vector , 4) #search area widened 
                ] 

    if dim1 >= dim2: grid_dim = dim1 # this is just to accommodate how i am making the polygon area, i know its werid
    else: grid_dim = dim2
    
    x, y = np.meshgrid(np.arange(grid_dim), np.arange(grid_dim)) # make a canvas with coordinates
    x, y = x.flatten(), y.flatten()
    points = np.vstack((x,y)).T 

    p = Path(tupVerts) # make a polygon
    grid = p.contains_points(points)
    mask = grid.reshape(grid_dim,-grid_dim) # now you have a mask with points inside a polygon

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
    
    #------------------------ combine information from boundary image with search zone of mask
    negative_image = get_negative_image( boundary_image) #black on white -> white on black
    #add borders
    for side in sides_list:
        negative_image = drawline(np.array(side[0]),np.array(side[1]),negative_image)
    
    # add extra buffer ? 
    top_side    = [(1,1) , (1,boundary_image.shape[1] -1 )]
    bottom_side = [(boundary_image.shape[0] -1,boundary_image.shape[1] -1) , (boundary_image.shape[0]-1 ,1) ]
    right_side  = [(1 ,boundary_image.shape[1] - 1) , (boundary_image.shape[0]-1,boundary_image.shape[1]-1)]
    left_side   = [(boundary_image.shape[0]-1,1) , (1,1)]
    
    sides_list = [top_side,bottom_side,right_side,left_side]
    for side in sides_list:
        negative_image = drawline(np.array(side[0]),np.array(side[1]),negative_image)
    
    mask = mask *255 #convert mask to integer array
    
    # show_image(negative_image)

    
    search_zone = np.zeros((boundary_image.shape[0],boundary_image.shape[1])) # get black background 
    for col in range(0,dim1):
        for row in range(0,dim2):
            if negative_image[col][row] > 0 and negative_image[col][row] == mask[col][row]:
                search_zone[col][row] = 255

    # show_image(search_zone) 

    # ----------------- find nearest white image! 
    a = find_nearest_white( search_zone, end_point) #find nearest object in search zone  
    b = start_point
    c = end_point
    
    distance_buffer = 6 # prevent the pixels from paths overlapping 
    distb = abs(np.linalg.norm(a-b)) - distance_buffer #this calculates euclidean distance between two points - a buffer
    distc = abs(np.linalg.norm(a-c)) - distance_buffer #this calculates euclidean distance between two points - a buffer
    if distb < distc: dist = distb # pick least distance
    else: dist = distc
    # dist = np.linalg.norm(a-b) #this   calculates euclidean  between two points 
    
    # print('distance is :', dist)
    
    zig_zag_size_vector = normalized_slope_vector * int(dist) # make the zig zag only as far as the closest boundary 

    # if dist <= 0: 
    #     print("warning: point at ", b , "distance from nearest boundary is ", dist , '\n')

    # ----------------------- below the actual zig zags happen 
    zig_zag_boundary_image =  get_negative_image(boundary_image)
    zig_zag_image = new_image
    
    line_array = [] #array to store points on the line
    
    if abs(dist) <= zig_zag_threshold:
        try : 
            zig_zag_image = drawline(start_point,end_point,zig_zag_image) # just draw a line startpoint to endpoint 
            
            # boundary_image = get_negative_image(boundary_image) #temporarily convert take negative - in future can just change drawline function 
            zig_zag_boundary_image = drawline(start_point,end_point,zig_zag_boundary_image) # just draw a line startpoint to endpoint
            # boundary_image = get_negative_image(boundary_image) #temporarily convert take negative - in future can just change drawline function 
        except : print("error zigging")

        line_array = get_line(start_point[0], start_point[1] , end_point[0] , end_point[1] )
        # if len(line_array):
        #     print("this is good")
        # else:
        #     print("this is not good ")

    elif abs(dist) > zig_zag_threshold:
        
        
        if i%2 ==0: # set zig and zag values (with alternating directions): this is basically creating zig zag vector perpendicular to the skeleton chunk input
            zigzag = [-zig_zag_size_vector[1], zig_zag_size_vector[0]]
        else:
            zigzag = [zig_zag_size_vector[1], -zig_zag_size_vector[0]]

        pt1 = start_point
        pt2 = start_point + zigzag
        pt3 = end_point
        
        try : zig_zag_image = drawline(pt1,pt2,zig_zag_image)
        except : print("error zigging")
        try : zig_zag_image = drawline(pt2,pt3,zig_zag_image)
        except : print("error zigging")
        try:
            # boundary_image = get_negative_image(boundary_image) #temporarily convert take negative - in future can just change drawline function 
            zig_zag_boundary_image = drawline(pt1,pt2,zig_zag_boundary_image) # zig zag on boundary 
            zig_zag_boundary_image = drawline(pt2,pt3,zig_zag_boundary_image) # zig zag on boundary
            # zig_zag_boundary_image = get_negative_image(boundary_image) #temporarily convert take negative - in future can just change drawline function 
        except : print("error zigging bound")
    
        line_1 = get_line(pt1[0], pt1[1] , pt2[0] , pt2[1] )
        line_2 = get_line(pt2[0], pt2[1] , pt3[0] , pt3[1] )
        # line_array = line_1 + line_2 # zig zagged line array
        line_array.extend(line_1)
        line_array.extend(line_2) # zig zagged line array
        # if len(line_1):
        #     print("this is good")
        # else:
        #     print("this is not good ")
        # if len(line_2):
        #     print("this is good")
        # else:
        #     print("this is not good ")

    zig_zag_boundary_image = get_negative_image(zig_zag_boundary_image)
    # show_image(boundary_image)
    # return(new_image,boundary_image)
    # print(boundary_image[0])
    return(zig_zag_image, zig_zag_boundary_image, line_array)  