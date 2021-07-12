import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")
from get_graph_distance import *

waypoint1 = [34.044469379652604,-81.20919780058651]
waypoint2 = [34.044469379652604,-81.20902519061583]
path = r'./MAPS/Lake_Murray_Map_Skeletons/e_d_murray_skeleton.png' 

get_graph_distance(waypoint1,waypoint2,path)

