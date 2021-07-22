
import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from jasons_skeletonize_from_array import * 
from open_or_show_image import *

#input path to image 
#output spits out many images saved to same enviornment (skeleton, lee, medial axis, thinned, partial thinned)
path = r'./MAPS/Map_originals/Ibrahim_Test/ibrahim_test_bw.png'

image = open_image(path)

med_axis , skeleton , skeleton_lee , thinned , thinned_partial = jasons_skeletonize_from_array(image)

skeletons = [med_axis , skeleton , skeleton_lee , thinned , thinned_partial]
for skel in skeletons:
    show_image(skel)