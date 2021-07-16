import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from inverse_skeletonize import *


# path = r'./MAPS/Lake_Murray_Map_Skeletons/e_d_image4.png' 

#inputs =  skeletonize_skeleton(path, weight_threshold) -- weight threshold is how much to trim the inv skeletons by
path = r'./MAPS/Map_Skeletons/Ibrahim_test_skeletons/preprocessing/trimmed/trimmed_e4_d4___MAPS_Map_originals_Ibrahim_Test_ibrahim_test_bw_png_png_skeleton_lee94_png.png' 
weight_threshold = 0

med_axis , skeleton , skeleton_lee , thinned , thinned_partial, name , paths_list = inverse_skeletonize(path, weight_threshold)