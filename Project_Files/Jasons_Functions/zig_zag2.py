

import cv2
import numpy as np

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from drawline import * 
from skeleton_to_graph import * # graph = skeleton_to_graph(path)
from open_or_show_image import * 

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



def zig_zag2(start_point,end_point,zig_zag_size,zig_zag_image,boundary_image, i ): #zigzagsize will scale the size of the zig zags
    #inputs: start_point,end_point,zig_zag_size,zig_zag_image,boundary_image, i
    #   i is just an integer, if even it will zig, if odd it will zag
    
    # boundary_image = (boundary_image > 0)
    
    slope_vector = np.array([  end_point[0]- start_point[0] , end_point[1] - start_point[1] ]) # vector representation of slope here in format [y , x]
    # step_vector = slope_vector / (num_turns - 1) # partition total change inslope into steps to zig zag across and -1 because the number of turns will be one less than the number of partitions (also in format [y , x])
    normalized_slope_vector = slope_vector/np.linalg.norm(slope_vector) # here we are getting the normalized step_vector so we can use its direction and ignore its magnitude 
    print(normalized_slope_vector)
    #------------------------ here i need to figure out how to know the zig zag size : sense the edge 
    
    negative_image = get_negative_image( boundary_image)
    
    a = find_nearest_white( negative_image, end_point) #this might have confusion of coordinate point paits 
    b = end_point
    print( a,b )
    
    dist = np.linalg.norm(a-b) #this calculates euclidean distance between two points 
    print(dist , '\n')
    zig_zag_size_vector = normalized_slope_vector * int(dist-.05) # make the zig zag only as far as the closest boundary 

    if dist == 0: 
        show_image ( negative_image)
    # print(zig_zag_size_vector)

    # ----------------------- below the actual zig zags happen 

    if i%2 ==0: # set zig and zag values (with alternating directions)
        zigzag = [-zig_zag_size_vector[1], zig_zag_size_vector[0]]
    else:
        zigzag = [zig_zag_size_vector[1], -zig_zag_size_vector[0]]

    pt1 = start_point
    pt2 = end_point + zigzag
    pt3 = end_point
    try : zig_zag_image = drawline(pt1,pt2,zig_zag_image)
    except : print("error zigging")
    try : zig_zag_image = drawline(pt2,pt3,zig_zag_image)
    except : print("error zigging")
    
    #image = drawline(start_point,end_point,image) #this is just for error checking, draw a line between start and end points 
    #show_image(image)
    # show_image(get_negative_image( boundary_image))
    return(zig_zag_image)



# future me : this is what happens --> make array of all pixels on perpedicular vector 
# make 1 directional --> only in direction of zig zag