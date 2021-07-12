import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from trim_edges import * # new_array = trim_edges(path,weight_threshold)



path = r'./MAPS/Lake_Murray_Map_Skeletons/e_d_murray_skeleton.png' 
weight_threshold = 30

trim_edges(path,weight_threshold)