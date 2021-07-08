import cv2
import numpy as np
from skimage.morphology import skeletonize
import sknw

#Jasons skeleton to graph function, useful for extracting information about skeleton 
# ------------------------------------------------------------------------
#inputs: path to skeleton of an image
#outputs: <class 'networkx.classes.graph.Graph'>
def skeleton_to_graph(path):
    try: img = cv2.imread(cv2.samples.findFile(path),0) # get img
    except : print("\n\ncan't find that image at", path,"\n\n")
    img = (255-img) 
    img = img > 127 #make bool 
    ske = skeletonize(~img).astype(np.uint16) # this just changes data type and SHOULDNT change skeleton shape
    graph = sknw.build_sknw(ske) # build graph from skeleton
    print("\nskeleton converted to graph\n")
    return graph

