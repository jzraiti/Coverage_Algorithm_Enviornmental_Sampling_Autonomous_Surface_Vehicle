
import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from jasons_skeletonize import * 


#input path to image 
#output spits out many images saved to same enviornment (skeleton, lee, medial axis, thinned, partial thinned)
path = r'./MAPS/Map_originals/Ibrahim_Test/ibrahim_test_bw.png'
med_axis , skeleton , skeleton_lee , thinned , thinned_partial, name , paths_list = jasons_skeletonize(path)


