import numpy as np

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from trim_edges import * # new_array = trim_edges(path,weight_threshold)
from open_or_show_image import * 
from erosion_dilation import * 



from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
from skimage.morphology import medial_axis
import cv2 
from skimage.morphology import thin


# path = r'./MAPS/Lake_Murray_Map_Skeletons/e_d_image4.png' 
path = r'./MAPS/Lake_Murray_Map_Skeletons/e_d_murray_skeleton.png' 

# -------------- get background of correct size
image = open_image(path) #numpy.ndarray (403,341) ->  (y,x) each y,x point has a value 225 or 0 
white_image = np.zeros((image.shape[0],image.shape[1])) # get black background 
# show_image(black_image)

# ---------------- get trimmed skeleton 
weight_threshold = 30
new_array = trim_edges( path,weight_threshold ) # NEW ARRAY IS IN Y,X format, as a nested list of graph[edges[x,ypos]]

# new_image = black_image +225
for edge in new_array:
    for point in edge:
        # print(point[0], point[1])
        white_image[point[0]][point[1]] = 225
        
show_image(white_image) # this is the inverse of thinned skel

cv2.imwrite('trim_skeleton.png', white_image)