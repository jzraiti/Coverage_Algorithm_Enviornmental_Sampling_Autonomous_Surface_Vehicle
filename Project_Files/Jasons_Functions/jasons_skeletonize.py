from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert

from skimage.morphology import medial_axis

import cv2 as cv 

from skimage.morphology import thin



def jasons_skeletonize(path):
    #read 3D rbg image as 2D greyscale nparray
    blobs = cv.imread(cv.samples.findFile(path),0) 
    # last parameter 0 = greyscale 1 = color -1 = unchanged 

    #convert data from int to np bool 
    blobs = blobs < 123

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

    cv.imwrite('_medial_axis.png', dist_on_skel * 30)
    cv.imwrite('_skeleton.png', skeleton * 255)
    cv.imwrite('_skeleton_lee94.png', skeleton_lee )
    cv.imwrite('_thinned.png', thinned * 255)
    cv.imwrite('_thinned_partial.png', thinned_partial * 255)
    return 0



# path = r'./MAPS/Map_originals/Ibrahim_Test/ibrahim_test_bw.png'
# Jasons_skeletonize(path)


