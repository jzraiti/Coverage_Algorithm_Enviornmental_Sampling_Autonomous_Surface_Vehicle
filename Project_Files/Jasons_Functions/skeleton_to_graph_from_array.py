import cv2
import numpy as np
from skimage.morphology import skeletonize
import sknw

from open_or_show_image import * 


#Jasons skeleton to graph function, useful for extracting information about skeleton 
# ------------------------------------------------------------------------
#inputs: path to skeleton of an image
#outputs: <class 'networkx.classes.graph.Graph'>
def skeleton_to_graph_from_array(image):
    """takes in image array , note needs to be black background white foreground , 
    from https://github.com/Image-Py/sknw
    
    :param path: path to image
    :type path: string

    :rtype: graph
    :return: a graph of the skeleton with 
    """
    
    # try: img = open_image(path)# get img
    # except : print("\n\ncan't find that image at", path,"\n\n")
    
    image = (255-image) 
    image = image > 127 #make bool 
    
    ske = skeletonize(~image).astype(np.uint16) # this just changes data type and SHOULDNT change skeleton shape
    graph = sknw.build_sknw(ske) # build graph from skeleton
    print("\nskeleton converted to graph\n")
    return graph

