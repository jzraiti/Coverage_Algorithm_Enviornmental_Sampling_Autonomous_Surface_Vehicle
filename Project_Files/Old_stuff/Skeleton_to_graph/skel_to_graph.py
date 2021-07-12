from skimage.morphology import skeletonize
from skimage import data
import sknw
import numpy as np
from matplotlib import pyplot as plt

import networkx as nx

import cv2 as cv

def skeleton_to_graph():

    path_to_map = "Lake_Murray_Map_Skeletons/SE_corner_thinned.png"
    img = cv.imread(cv.samples.findFile(path_to_map),0)

    img = img > 127 

    print(img)
    ske = skeletonize(~img).astype(np.uint16)

    # build graph from skeleton
    graph = sknw.build_sknw(ske)

    # draw image
    plt.imshow(img, cmap='gray')

    print(graph.edges())
    # draw edges by pts
    for (s,e) in graph.edges():
        print(s,e)

skeleton_to_graph()
