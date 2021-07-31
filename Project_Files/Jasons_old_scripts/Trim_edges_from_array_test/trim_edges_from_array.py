#Jasons script for trimming edges 

import matplotlib.pyplot as plt

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from skeleton_to_graph import * # graph = skeleton_to_graph(path)
from open_or_show_image import * # image = open_image(path) , show_image(image)
from locate_nodes import * # total_skeleton,node_locations,edge_locations,endpoint_locations,island_locations = locate_nodes(path)

def trim_edges(path,weight_threshold):

    graph = skeleton_to_graph(path)
    image = open_image(path) #start by opening the image, choose image in the function 
    total_skeleton,node_locations,edge_locations,endpoint_locations,island_locations = locate_nodes(path)

    new_array_just_edges= []
    trimmed = []

    graph = skeleton_to_graph(path)
    
    for (s,e) in graph.edges():
        
        ps = graph[s][e]['pts']
        start = [ ps[0,1],ps[0,0] ]
        end = [ ps[-1,1],ps[-1,0] ]
        
        if ( (start in endpoint_locations) or (end in endpoint_locations) ): # ------weight < theshold AND endpoints are not nodes
            # print('edge found')  
            if graph[s][e]['weight'] < weight_threshold:
                
                # print('trim this one')
                trimmed.append(graph[s][e]['pts'])
                plt.plot(ps[:,1], ps[:,0], 'green')
            else:
                # print('nah leave em be')
                new_array_just_edges.append(graph[s][e]['pts'])
                plt.plot(ps[:,1], ps[:,0], 'red')
        else:
            # print("no matches")
            new_array_just_edges.append(graph[s][e]['pts'])
            plt.plot(ps[:,1], ps[:,0], 'red')

    plt.imshow(image, cmap='gray') #map the image to black and white, white representing the line 

    # name = 'trimmed_' + str(path)
    # name = name.replace("/", "_")
    # name = name.replace(".", "_")
    # name = str(name) + '.png' 
    # plt.savefig(name, format="png")
    
    plt.show()


    # ------- make new "image array" that can be written using cv2 -----
    black_image = np.zeros((image.shape[0],image.shape[1])) # get black background 

    # ---------------- get trimmed skeleton 
    new_image = black_image
    for edge in new_array_just_edges:
        for point in edge:
            # print(point[0], point[1])
            new_image[point[0]][point[1]] = 255
    
    return new_array_just_edges , new_image
