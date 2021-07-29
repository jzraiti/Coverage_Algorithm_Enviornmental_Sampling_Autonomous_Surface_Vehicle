import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")
from skeleton_to_graph import *
from generate_waypoints import *

def get_graph_distance(waypoint1,waypoint2,path):
    print("\nfrom generate_waypoints: be sure that waypoint 1 and 2 are adjacent aka have either same longitude or latitude \n")
    #notes: csv file can be uploaded to google maps to find (on my maps ), you can edit as a layer
    
    unit_distance = find_distance(waypoint1,waypoint2)
    graph = skeleton_to_graph(path) #path = path to skeleton
    weight_sum = 0
    for (s,e) in graph.edges():
        # if graph[s][e]['weight'] > 30: # ------------------------------------------------- this is to make the small edges not apply 
        weight = graph[s][e]['weight']
        weight_sum = weight_sum + weight
    total_distance = weight_sum * unit_distance
    print("\n\ntotal distance of graph at ", path, " \n\n(in meters) is" ,total_distance)
    return total_distance, weight_sum , unit_distance

