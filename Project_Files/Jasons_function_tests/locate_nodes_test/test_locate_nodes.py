import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from locate_nodes import * # total_skeleton,node_locations,edge_locations,endpoint_locations,island_locations = locate_nodes(path)


path = r'./MAPS/Lake_Murray_Map_Skeletons/e_d_murray_skeleton.png' 

total_skeleton,node_locations,edge_locations,endpoint_locations,island_locations = locate_nodes(path)