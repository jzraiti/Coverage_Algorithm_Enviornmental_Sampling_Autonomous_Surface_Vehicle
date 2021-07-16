


import numpy as np

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from zig_zag import * 

from skeleton_to_graph import * 

from open_or_show_image import * 



path = r'./MAPS/Map_Skeletons/Ibrahim_test_skeletons/preprocessing/trimmed/trimmed_e4_d4___MAPS_Map_originals_Ibrahim_Test_ibrahim_test_bw_png_png_skeleton_lee94_png.png' 
graph = skeleton_to_graph(path)



nodes = graph.nodes()
ps = np.array([nodes[i]['o'] for i in nodes]) # extract coodinates for each node 
# ps[0,1], ps[0,0] = x , y coordinates for node 0  



image = open_image(path) #start by opening the image, choose image in the function 

for (s,e) in graph.edges():

    start_point = np.array([ ps[s,0] , ps[s,1] ]) #list[] vs tuple() coordinates y , x 
    end_point = np.array([  ps[e,0] , ps[e,1]  ])
    image = zig_zag(start_point,end_point,10,graph[s][e]['weight']/2,image)

show_image(image)
cv2.imwrite('zigzag_full.png', image )






