import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from erosion_dilation import * 



# path to image
path = r'./inverse_skeletons/e1_d0_negative_skeleton_png_png_medial_axis.png'
option = 2 # 1 = erode first 2 = dialate first 
num_erosions = 0
num_dilations = 1

# inputs = path to image, erode first (1) or dialate first (2) .desired number of erosions, desired number of dialations 
# outputs = eroded then dialated image
e_d_image , name = erosion_dilation(path,option,num_erosions,num_dilations)
print(name )