import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from find_starting_node import *


from open_or_show_image import * 

from postman_problems.solver import cpp

from postman_problems.stats import calculate_postman_solution_stats

# PRAISE BE TO https://github.com/brooksandrew/postman_problems#python


def chinese_post_man(path_to_skel,config_file,launch_point, path_to_csv):
    """finds best path across skeleton, returning to launch point
    
    :param path_to_skel: path to image  of full zig zag
    :type path_to_skel: string
    :param config: file containing essential information about area of operation such as coordinates
    :type config: text file 
    :param launch point: estimated coordinates (lat long) of launching point
    :type path_to_skel: float array
    :param path_to_csv: path to file created by write_chinese_post_man.py
    :type path_to_csv: string  
    
    :rtype: circuit and graph are lists 
    :return: the path to follow along the skeleton 
    """
    #find start node 
    starting_node, starting_node_xy = find_starting_node(path_to_skel, config_file, launch_point )

    #calculate best path
    circuit, graph = cpp(edgelist_filename= str(path_to_csv), start_node=str(starting_node))

    return circuit, graph