import numpy as np

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from drawline import * 

from erosion_dilation import * 

from jasons_skeletonize import * 

from trim_edges import * # new_array = trim_edges(path,weight_threshold)

from generate_waypoints import *

from skeleton_to_graph import * # graph = skeleton_to_graph(path)

from open_or_show_image import * # image = open_image(path) , show_image(image)

from locate_nodes import * # total_skeleton,node_locations,edge_locations,endpoint_locations,island_locations = locate_nodes(path)


from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
from skimage.morphology import medial_axis
import cv2 
from skimage.morphology import thin


# path = r'./MAPS/Lake_Murray_Map_Skeletons/e_d_image4.png' 
path = r'./MAPS/Map_Skeletons/Ibrahim_test_skeletons/preprocessing/trimmed/trimmed_e4_d4___MAPS_Map_originals_Ibrahim_Test_ibrahim_test_bw_png_png_skeleton_lee94_png.png' 

# -------------- get background of correct size
image = open_image(path) #numpy.ndarray (403,341) ->  (y,x) each y,x point has a value 225 or 0 
black_image = np.zeros((image.shape[0],image.shape[1])) # get black background 
white_image = black_image +255 #convert to white 

# ---------------- get trimmed skeleton 
weight_threshold = 30
new_array, new_image = trim_edges( path,weight_threshold ) # NEW ARRAY IS IN Y,X format, as a nested list of graph[edges[x,ypos]]


for edge in new_array:
    for point in edge:
        print('\nhere ',point[0], point[1])
        white_image[point[0]][point[1]] = 0
        
show_image(white_image) # this is the inverse of thinned skel

cv2.imwrite('negative_skeleton.png', white_image)
#--------------------------------------------------- do erosion and dilation

# path to image
path = r'negative_skeleton.png'
option = 1 
num_erosions = 1
num_dilations = 0

# inputs = path to image, erode first (1) or dialate first (2) .desired number of erosions, desired number of dialations 
# outputs = eroded then dialated image
e_d_image , name = erosion_dilation(path,option,num_erosions,num_dilations)

cv2.imwrite('e_d_image.png', e_d_image )

#-------------------------------------------------- get thinnned skel of skel

blobs = open_image('e_d_image.png')
blobs = blobs > 127

thinned = thin(blobs)
thinned_partial = thin(blobs, max_iter=10)

fig, axes = plt.subplots(2, 1, figsize=(8, 8), sharex=True, sharey=True)
#fig, axes = plt.subplots(1, 2)
ax = axes.ravel()


ax[0].imshow(thinned, cmap=plt.cm.gray)
ax[0].set_title('thinned')
ax[0].axis('off')

ax[1].imshow(thinned_partial, cmap=plt.cm.gray)
ax[1].set_title('partially thinned')
ax[1].axis('off')

fig.tight_layout()
plt.show()

cv2.imwrite('_thinned.png', thinned * 255)
cv2.imwrite('_thinned_partial.png', thinned_partial * 255)

# ---------------------------------------------------- lets try the other skeleton methods 

# Compute the medial axis (skeleton) and the distance transform
skel, distance = medial_axis(blobs, return_distance=True)

# Compare with other skeletonization algorithms
skeleton = skeletonize(blobs)
skeleton_lee = skeletonize(blobs, method='lee')

# Distance to the background for pixels of the skeleton
dist_on_skel = distance * skel

fig, axes = plt.subplots(2, 2, figsize=(8, 8), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(blobs, cmap=plt.cm.gray)
ax[0].set_title('original')
ax[0].axis('off')

ax[1].imshow(dist_on_skel, cmap='hot')
ax[1].contour(blobs, [0.5], colors='w')
ax[1].set_title('medial_axis')
ax[1].axis('off')

ax[2].imshow(skeleton, cmap=plt.cm.gray)
ax[2].set_title('skeletonize')
ax[2].axis('off')

ax[3].imshow(skeleton_lee, cmap=plt.cm.gray)
ax[3].set_title("skeletonize (Lee 94)")
ax[3].axis('off')

fig.tight_layout()
plt.show()

cv2.imwrite('_medial_axis.png', dist_on_skel * 30)
cv2.imwrite('_skeleton.png', skeleton * 255)
cv2.imwrite('_skeleton_lee94.png', skeleton_lee )

# print(dist_on_skel.shape)
# for i in dist_on_skel:
#     print(i)