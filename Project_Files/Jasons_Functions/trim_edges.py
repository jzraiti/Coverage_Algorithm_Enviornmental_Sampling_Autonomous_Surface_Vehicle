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

    new_array= []
    trimmed = []

    graph = skeleton_to_graph(path)
    
    
    


    for (s,e) in graph.edges():
        
        ps = graph[s][e]['pts']
        start = [ ps[0,1],ps[0,0] ]
        end = [ ps[-1,1],ps[-1,0] ]
        
        
        # print(graph[s][e]['weight'] < weight_threshold )
        
        
        if ( (start in endpoint_locations) or (end in endpoint_locations) ): # ------weight < theshold AND endpoints are not nodes
            # print('edge found')  
            if graph[s][e]['weight'] < weight_threshold:
                
                # print('trim this one')
                trimmed.append(graph[s][e]['pts'])
                plt.plot(ps[:,1], ps[:,0], 'green')
            else:
                # print('nah leave em be')
                new_array.append(graph[s][e]['pts'])
                plt.plot(ps[:,1], ps[:,0], 'red')
        else:
            # print("no matches")
            new_array.append(graph[s][e]['pts'])
            plt.plot(ps[:,1], ps[:,0], 'red')
            
    # also implement visualization the check trimming results : uncomment below - or make this an argument
    # print("\n\nfrom trim_edges:")
    # print("trimmed edges will be shown in red")
    # print("retained edges will be shown in green")
    # print("trimmed" , trimmed)
    
    # show_image(image)
    plt.imshow(image, cmap='gray') #map the image to black and white, white representing the line 

    name = 'trimmed_' + str(path)
    name = name.replace("/", "_")
    name = name.replace(".", "_")
    name = str(name) + '.png' 
    # plt.savefig(name, format="png")
    
    plt.show()


    # ------- make new "image array" that can be written using cv2 -----
    # image = open_image(path) #numpy.ndarray (403,341) ->  (y,x) each y,x point has a value 225 or 0 
    black_image = np.zeros((image.shape[0],image.shape[1])) # get black background 
    # show_image(black_image)

    # ---------------- get trimmed skeleton 
    # weight_threshold = 30
    # new_array = trim_edges( path,weight_threshold ) # NEW ARRAY IS IN Y,X format, as a nested list of graph[edges[x,ypos]]

    # new_image = black_image +225
    new_image = black_image
    for edge in new_array:
        for point in edge:
            # print(point[0], point[1])
            new_image[point[0]][point[1]] = 225
    
    
    
    # show_image(new_image) # this is the inverse of thinned skel

    # cv2.imwrite(name, new_image)


    return new_array , new_image
