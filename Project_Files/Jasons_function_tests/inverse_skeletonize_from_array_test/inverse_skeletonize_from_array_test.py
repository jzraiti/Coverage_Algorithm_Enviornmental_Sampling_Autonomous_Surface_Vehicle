import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from inverse_skeletonize_from_array import *
from open_or_show_image import *

path = r'./MAPS/Map_Skeletons/Ibrahim_test_skeletons/preprocessing/trimmed/trimmed_e4_d4___MAPS_Map_originals_Ibrahim_Test_ibrahim_test_bw_png_png_skeleton_lee94_png.png' 
image = open_image(path)

med_axis , skeleton , skeleton_lee , thinned , thinned_partial = inverse_skeletonize_from_array(image)

inverse_skeletons = [med_axis , skeleton , skeleton_lee , thinned , thinned_partial]
for inv_skel in inverse_skeletons:
    show_image(inv_skel)