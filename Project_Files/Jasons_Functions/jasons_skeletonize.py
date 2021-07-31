from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert

from skimage.morphology import medial_axis

import cv2 as cv 

from skimage.morphology import thin



def jasons_skeletonize(path):
    """takes in path to thresholded bw image, skeletonizes,and saves skeletons as image files 
    
    :param path: path to image
    :type path: string
    
    :rtype: skeleton image arrays, the naming conventions, and list of names/paths
    :return: med_axis , skeleton , skeleton_lee , thinned , thinned_partial , name , paths_list
    """
    
    #read 3D rbg image as 2D greyscale nparray
    blobs = cv.imread(cv.samples.findFile(path),0) 
    # last parameter 0 = greyscale 1 = color -1 = unchanged 

    #convert data from int to np bool 
    blobs = blobs > 123 # BIGNOTE: this is made for skeletonization when the white area is the desired area for skeletonization

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
    
    #create name for files
    name = str(path)
    name = name.replace("/", "_")
    name = name.replace(".", "_")
    # print(name)
    
    med_axis = dist_on_skel * 255 # THESE scalars what do they do? 
    skeleton = skeleton * 255
    #skeleton_lee
    thinned = thinned * 255
    thinned_partial = thinned_partial * 255
    cv.imwrite(name + '_medial_axis.png', med_axis)
    cv.imwrite(name + '_skeleton.png', skeleton)
    cv.imwrite(name + '_skeleton_lee94.png', skeleton_lee )
    cv.imwrite(name + '_thinned.png', thinned)
    cv.imwrite(name + '_thinned_partial.png', thinned_partial)
    
    paths_list = [name + '_medial_axis.png' , name + '_skeleton.png' ,   name + '_skeleton_lee94.png' , name + '_thinned.png' ,  name + '_thinned_partial.png'   ]
    return med_axis , skeleton , skeleton_lee , thinned , thinned_partial , name , paths_list

