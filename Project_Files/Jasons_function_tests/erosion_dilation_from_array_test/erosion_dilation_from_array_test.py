import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from erosion_dilation_from_array import * 
from open_or_show_image import *



# path to image
path = r'./MAPS/Map_Skeletons/Ibrahim_test_skeletons/no_preprocessing/Ibrahim_medial_axis.png'
# Reading an image in default mode
image = open_image(path)

option = 2 # 1 = erode first 2 = dialate first 
num_erosions = 1
num_dilations = 5

# inputs = path to image, erode first (1) or dialate first (2) .desired number of erosions, desired number of dialations 
# outputs = eroded then dialated image
e_d_image = erosion_dilation_from_array(image,option,num_erosions,num_dilations)

show_image(e_d_image)