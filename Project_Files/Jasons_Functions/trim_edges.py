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
        
        
        print(graph[s][e]['weight'] < weight_threshold )
        
        
        if ( (start in endpoint_locations) or (end in endpoint_locations) ): # ------weight < theshold AND endpoints are not nodes
            print('edge found')  
            if graph[s][e]['weight'] < weight_threshold:
                
                print('trim this one')
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
    print("\n\nfrom trim_edges:")
    print("trimmed edges will be shown in red")
    print("retained edges will be shown in green")
    print("trimmed" , trimmed)
    show_image(image)
    plt.show()
    # plt.savefig('trimmed_results.pdf')

    return new_array