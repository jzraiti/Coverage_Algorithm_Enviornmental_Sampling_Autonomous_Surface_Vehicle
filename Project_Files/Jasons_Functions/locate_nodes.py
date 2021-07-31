import cv2

#Jasons script for gathering data directly from image of skeleton, specifically finding nodes

def locate_nodes(path_to_image):
    '''
    Old manual function to try and locate the main features of a skeleton:
    Takes in path to image, outputs node locations and other information, though test it before using
    There have been edge cases where this function breaks which is why I have largly avoided using it except in trim edges
    (which I could probably change)
    '''
    blobs = cv2.imread(cv2.samples.findFile(path_to_image),0) 

    #convert data from int to np bool 
    blobs = blobs > 127 

    ydim = blobs.shape[0] #num rows 540
    xdim = blobs.shape[1] #num columns 960


    # measure some skeleton metrics down here 
    sum_local_neighbors = 0 #number of adjacent skeleton pixels 
    sum_num_nodes = 0 #total number pixels that are of nodes of the skeleton
    sum_num_edges = 0 #total number pixels that are of edges ots 
    sum_num_endpoints = 0 #total number of pixels that are end points of the skeleton
    sum_num_islands = 0 #total number of pixels that are isolated
    sum_points_length = 0 #total number of skeleton pixels aka length of skeleton

    total_num_edgelines = 0 #how many actual edges are there in the network

    #lets make a bunch of arrays storing : node locations, endpoint locations, edge locations,island locations  
    node_locations = []
    edge_locations = []
    endpoint_locations = []
    island_locations = []

    total_skeleton = []
    #here we are going to find the nodes and edges and endpoints

    for row in range(0,ydim): #iterate through rows 
        for col in range(0,xdim): #iterate through columns
            
            if blobs[row][col] == True: #if pixel is skeleton add 1 to length of skeleton
                sum_points_length +=1
                
                #find the sum of the local neighbors included in the skeleton (including self): 1 = solo ,2= endpointa3 = edge , 4+ = node 
                for i in range(-1,2):
                    for j in range(-1,2):
                        try: #this because there may be points on the edge of the picturetotal_skeleton,node_location,edge_locations,endpoint_locations,island_locations
                                sum_local_neighbors += int(blobs[row +i][col +j])
                        except:
                            pass
                
                #HEY JUST SO YOU KNOW: here I switch formats from (y,x) to (x,y) just to make things more confusing 
                
                #figure out num nodes endpoints and edges
                if sum_local_neighbors >= 4: #if node
                    node_locations.append([col,row])
                    sum_num_nodes += 1
                    total_num_edgelines += sum_local_neighbors -1 #count connection points (-1 to remove self counting)
                elif sum_local_neighbors == 3: # if edge
                    edge_locations.append([col,row])
                    sum_num_edges += 1
                elif sum_local_neighbors == 2: # if endpoint
                    endpoint_locations.append([col,row])
                    sum_num_endpoints += 1
                    total_num_edgelines += sum_local_neighbors -1 #count connection points (-1 to remove self counting)
                else: #if island 
                    island_locations.append([col,row])
                    print("isolated point at (x,y)", col, row)
                    sum_num_islands +=1
                total_skeleton.append([col,row])
                #reset counter     
                sum_local_neighbors = 0

    #error check
    if sum_num_nodes + sum_num_edges + sum_num_endpoints + sum_num_islands == sum_points_length & len(total_skeleton) == sum_points_length:
        print("No errors detected")
    else:
        print("f*&! something went wrong in locate nodes ")

    total_num_edgelines = total_num_edgelines / 2 #because each edge has two endpoints 
    # print("this skeleton has {0} edge lines, {1} nodes, {2} endpoints, and {3} islands. \nthe skeleton is of length {4} pixels.".format(total_num_edgelines , sum_num_nodes, sum_num_endpoints, sum_num_islands, sum_points_length))

    # print("the edgelines are of average length (in pixels) {0}, .".format( sum_num_edges / total_num_edgelines))

    # print("this function returns total_skeleton, nodes, edges, endpoints, and island's locations in (x,y) coordinate form\n\n\n")
    return total_skeleton,node_locations,edge_locations,endpoint_locations,island_locations

