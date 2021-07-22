from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert

from skimage.morphology import medial_axis

import cv2 as cv 

from skimage.morphology import thin



def jasons_skeletonize_from_array(image):

    #convert data from int to np bool 
    blobs = image > 123 # BIGNOTE: this is made for skeletonization when the white area is the desired area for skeletonization

    # Compute the medial axis (skeleton) and the distance transform
    skel, distance = medial_axis(blobs, return_distance=True)

    # Compare with other skeletonization algorithms
    skeleton = skeletonize(blobs)
    skeleton_lee = skeletonize(blobs, method='lee')

    # Distance to the background for pixels of the skeleton
    dist_on_skel = distance * skel

    # create thinned skeleton
    thinned = thin(blobs)
    thinned_partial = thin(blobs, max_iter=40)
    
    med_axis = dist_on_skel >0 # THESE scalars what do they do? 
    med_axis = med_axis *255
    
    skeleton = skeleton * 255
    thinned = thinned * 255
    thinned_partial = thinned_partial * 255
    
    return med_axis , skeleton , skeleton_lee , thinned , thinned_partial 


