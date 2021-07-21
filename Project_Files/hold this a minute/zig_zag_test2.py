import cv2 
import numpy as np

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from zig_zag2 import * #inputs: start_point,end_point,zig_zag_size,zig_zag_image,boundary_image, i
    #   i is just an integer, if even it will zig, if odd it will zag

from skeleton_to_graph import * 

from open_or_show_image import * 



path1 = r'./MAPS/Map_Skeletons/Ibrahim_test_skeletons/preprocessing/trimmed/trimmed_e4_d4___MAPS_Map_originals_Ibrahim_Test_ibrahim_test_bw_png_png_skeleton_lee94_png.png' 
graph = skeleton_to_graph(path1)
skel_image = open_image(path1) #start by opening the image, choose image in the function 

path2 = r'./overlay_boundary_image.png'
boundary_image = open_image(path2)



nodes = graph.nodes()
ps = np.array([nodes[i]['o'] for i in nodes]) # extract coodinates for each node 
# ps[0,1], ps[0,0] = x , y coordinates for node 0  

new_image = np.zeros((boundary_image.shape[0],boundary_image.shape[1])) # get black background 

for (s,e) in graph.edges():

    # print(int(graph[s][e]['weight'] /10) , int( len ( graph[s][e]['pts']  ) / 10))
    points = graph[s][e]['pts']
    num_points = len(points)
    weight = graph[s][e]['weight']
    zag_length = 10
    
    x = int( (num_points - num_points%10) /10 ) # this is to prevent the chunks of the line going past the endpoint
    # print(x)
    
    for i in range(0 , x-1 ):

        
        start_point = np.array([ points[ i  * zag_length  ][0] , points[ i * zag_length  ][1] ])
        end_point   = np.array([ points[ (i+1) * zag_length ][0] , points[ (i+1) * zag_length  ][1] ])
        # print("start point = ", start_point)
        
        image = zig_zag2(  start_point  ,  end_point  , boundary_image , new_image, i)
        # start_point,end_point,zig_zag_image,boundary_image, i 
        # show_image(image)

    
    # print(int( len ( graph[s][e]['pts']  ) / 10)) # a list of tuples 
    # print(len ( graph[s][e]['pts']  ) / 10) # a list of tuples 

    # print( graph[s][e]['pts'][0][0]  ) #can be indexed like this!

    # start_point = np.array([ ps[s,0] , ps[s,1] ]) #list[] vs tuple() coordinates y , x !!!!!!!!!!!!!!!!!!!
    # end_point = np.array([  ps[e,0] , ps[e,1]  ])
    # image = zig_zag2(  start_point  ,  end_point  ,  int(graph[s][e]['weight'] /10)  ,  graph[s][e]['weight']/10  ,  skel_image  , boundary_image )



show_image(image)

cv2.imwrite('zigzag_full.png', image )


