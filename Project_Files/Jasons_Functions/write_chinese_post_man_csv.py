import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from skeleton_to_graph_from_array import * 

from open_or_show_image import * 

import os

def write_chinese_post_man_csv(data, option, name):
    """takes either path or array, option specifies which, writes a csv file
        
    :param input: path to image or image array of full zig zag
    :type path: string or array
    :param option: 1=path first or 2=array   
    :type option: int
    :param name: name of output csv file
    :type name: str
    
    :rtype: str
    :return: path to new csv file
    """
    # path to image
    if option==1:
        image = open_image(data)
    else:
        image = data
    graph = skeleton_to_graph_from_array(image)

    #write csv in proper format 

    mission_file = open(str(name), 'w')
    mission_file.write("node1,node2,distance\n")

    for s,e in graph.edges():
        output = str(s) + ',' + str(e) + ',' + str(graph[s][e]['weight']) + '\n'
        mission_file.write(output)
        # print(s,e,graph[s][e]['weight'])
    mission_file.close()
    print("done")
    return  os.path.realpath(mission_file.name) #return path to new csv file 
