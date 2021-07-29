import numpy as np

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from convert_coordinates import *

from skeleton_to_graph_from_array import * 

import matplotlib.pyplot as plt

from open_or_show_image import * 

import networkx as nx


def find_starting_node_from_graph(graph, config_file, launch_point ):
    """finds best starting point
    
    :param graph: graph of original skeleton
    :type path: networkx graph
    :param config: file containing essential information about area of operation such as coordinates
    :type config: text file 
    :param launch point: estimated coordinates (lat long) of launching point
    :type launch point: float array
    
    :rtype: int , int array coordinates
    :return: starting node number , coordinates 
    """
    # --- calculate launch poing 
        # '''convert_latlong_to_xy
        # Input: LONG LAT and config file !!!!!!!!!!!!!!!!!!!!!!!!!1 LONG LAT I SAY 
        # Output: x and y coordinates
        # Method: converts LONG LAT to x y
        # '''
    launch_point = convert_latlong_to_xy(launch_point[1], launch_point[0],config_file)
    print("launching from :", launch_point)
    # -- calculate starting node
    nodes = graph.nodes()
    # print(nodes[0],nodes[0]['o']) # nodes[node#]['o'] = [x,y]

    launch_point = np.array(launch_point)
    starting_node = 0
    starting_node_xy = []
    distance = 10**10
    for i in range(0,len(nodes)):
        temp_node_xy = np.array([nodes[i]['o'][1] , nodes[i]['o'][0]])
        temp_distance = abs(np.linalg.norm( launch_point - temp_node_xy  )) # gotta be really careful since the nodes are in yx format god only knows why
        if temp_distance < distance:
            distance = temp_distance
            starting_node = i
            starting_node_xy = temp_node_xy

    print("starting node, distance, xy: ", starting_node, distance, starting_node_xy)

    #--- plot to check 


    plt.figure()
    #plot launch point 
    plt.plot(launch_point[0],launch_point[1], 'r.')
    
        # plt.plot(launch_point[0],launch_point[1], 'r.')

    
    plt.annotate("launch point", # this is the text
                    (launch_point[0],launch_point[1]), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
    #plot starting node
    plt.plot(starting_node_xy[0],starting_node_xy[1], 'r.')
    
            # plt.plot(starting_node_xy[0],starting_node_xy[1], 'r.')

    
    plt.annotate(str(starting_node), # this is the text
                    (starting_node_xy[0],starting_node_xy[1]), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
    # draw image
    for (s,e) in graph.edges():
        ps = graph[s][e]['pts']
        plt.plot(ps[:,1], ps[:,0], 'green')
        

    # plt.imshow(image)
    plt.show()
    return starting_node, starting_node_xy

