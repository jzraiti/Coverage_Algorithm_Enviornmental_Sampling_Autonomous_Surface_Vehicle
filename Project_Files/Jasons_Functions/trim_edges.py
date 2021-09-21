#Jasons script for trimming edges 

import matplotlib.pyplot as plt

# import sys
# sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from skeleton_to_graph import * # graph = skeleton_to_graph(path)
from open_or_show_image import * # image = open_image(path) , show_image(image)
from locate_nodes import * # total_skeleton,node_locations,edge_locations,endpoint_locations,island_locations = locate_nodes(path)

def trim_edges(path,weight_threshold):
    """takes in path to image and weight threshold to trim from 
        
    :param path: path to image
    :type path: string
    :param weight_threshold: the threshold number of pixels and edge needs to be trimmed
    :type option: int

    :rtype: new_array = an array of just the points on retained edges , new_image = the complete image array including background area
    :return: edge and image arrays with trimmed edges
    """
    graph = skeleton_to_graph(path)
    image = open_image(path) #start by opening the image, choose image in the function 
    total_skeleton,node_locations,edge_locations,endpoint_locations,island_locations = locate_nodes(path)

    new_array= []
    trimmed = []

    graph = skeleton_to_graph(path)
    
    for (s,e) in graph.edges():
        
        ps = graph[s][e]['pts']
        start = [ ps[0,1],ps[0,0] ]
        end = [ ps[-1,1],ps[-1,0] ]
        
        if ( (start in endpoint_locations) or (end in endpoint_locations) ): # ------weight < theshold AND endpoints are not nodes
            # print('edge found')  
            if graph[s][e]['weight'] < weight_threshold:
                
                #print('trim this one')
                trimmed.append(graph[s][e]['pts'])
                plt.plot(ps[:,1], ps[:,0], 'green')
            else:
                #print('nah leave em be')
                new_array.append(graph[s][e]['pts'])
                plt.plot(ps[:,1], ps[:,0], 'red')
        else:
            #print("no matches")
            new_array.append(graph[s][e]['pts'])
            plt.plot(ps[:,1], ps[:,0], 'red')

    plt.imshow(image, cmap='gray') #map the image to black and white, white representing the line 

    # name = 'trimmed_' + str(path)
    # name = name.replace("/", "_")
    # name = name.replace(".", "_")
    # name = str(name) + '.png' 
    # plt.savefig(name, format="png")
    
    plt.show()

    ''' THIS IS THE OLD WAY OF DOING IT
        # ------- make new "image array" that can be written using cv2 -----
    black_image = np.zeros((image.shape[0],image.shape[1])) # get black background 

    # ---------------- get trimmed skeleton 
    new_image = black_image
    for edge in new_array:
        for point in edge:
            # print(point[0], point[1])
            new_image[point[0]][point[1]] = 255
    '''

    


    #lets try doing this the opposite way and only take out pixels marked for being trimmed
    trimmed_image = image # get original image
    for edge in trimmed:
        for point in edge:
            trimmed_image[point[0]][point[1]] = 0

    new_image = trimmed_image
    print("warning from trim_edges: new_array return value is no longer accurate")
    return new_array , new_image
