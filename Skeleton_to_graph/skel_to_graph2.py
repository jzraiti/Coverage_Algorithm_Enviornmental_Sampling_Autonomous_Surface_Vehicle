from skimage.morphology import skeletonize
from skimage import data
import sknw
import numpy as np
from matplotlib import pyplot as plt

import networkx as nx

import cv2 as cv

def skeleton_to_graph(path):
    try: img = cv.imread(cv.samples.findFile(path),0) # get img
    except : print("can't find that image at", path)
    img = img > 127 #make bool 
    ske = skeletonize(~img).astype(np.uint16) # use sknw skeletonize 
    graph = sknw.build_sknw(ske) # build graph from skeleton
    print("\nskeleton converted to graph\n")
    return graph


path = r"Lake_Murray_Map_Skeletons/SE_corner_thinned.png"
graph = skeleton_to_graph(path)

# draw edges by pts
for (s,e) in graph.edges():
    print(s,e)
