import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")
from get_graph_distance import *

# waypoint1 = [34.044469379652604,-81.20919780058651]
# waypoint2 = [34.044469379652604,-81.20902519061583]
# path = r'./MAPS/Lake_Murray_Map_Skeletons/e_d_murray_skeleton.png' 




waypoint1 = [34.029880745341615, -81.24450899696049]
waypoint2 = [34.02980962732919, -81.24450899696049]

path = r'./MAPS/Map_Skeletons/Ibrahim_test_skeletons/preprocessing/trimmed/trimmed_e4_d4___MAPS_Map_originals_Ibrahim_Test_ibrahim_test_bw_png_png_skeleton_png.png' 




get_graph_distance(waypoint1,waypoint2,path)

