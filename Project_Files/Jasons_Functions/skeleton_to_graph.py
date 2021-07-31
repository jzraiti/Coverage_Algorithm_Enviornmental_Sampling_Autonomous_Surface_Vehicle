import cv2
import numpy as np
from skimage.morphology import skeletonize
import sknw

from open_or_show_image import * 


#Jasons skeleton to graph function, useful for extracting information about skeleton 
# ------------------------------------------------------------------------
#inputs: path to skeleton of an image
#outputs: <class 'networkx.classes.graph.Graph'>
def skeleton_to_graph(path):
    """takes in path to image , note needs to be black background white foreground , 
    :param path: path to image
    :type path: string

    :rtype: graph
    :return: a graph of the skeleton with 
    """
    
    try: img = open_image(path)# get img
    except : print("\n\ncan't find that image at", path,"\n\n")
    img = (255-img) 
    img = img > 127 #make bool 
    ske = skeletonize(~img).astype(np.uint16) # this just changes data type and SHOULDNT change skeleton shape
    graph = sknw.build_sknw(ske) # build graph from skeleton
    # print("\nskeleton converted to graph\n")
    return graph

