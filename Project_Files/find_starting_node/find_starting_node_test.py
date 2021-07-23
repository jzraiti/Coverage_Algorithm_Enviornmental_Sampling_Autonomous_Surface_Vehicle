import sys

sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from find_starting_node import *

from open_or_show_image import * 


path = r'./find_starting_node/zigzag_full.png'

config_file = "find_starting_node/ibrahim_find_starting_node_config.wf" #config file 
launch_point = (34.02675, -81.2253)


starting_node, starting_node_xy = find_starting_node(path, config_file, launch_point )