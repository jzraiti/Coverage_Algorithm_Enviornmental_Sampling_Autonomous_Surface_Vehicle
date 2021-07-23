from os import path
import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from chinese_post_man import *

from write_chinese_post_man_csv import *

from open_or_show_image import * 

# PRAISE BE TO https://github.com/brooksandrew/postman_problems#python

# make csv file with all nodes for chinese post man



#inputs
path_to_skel = r'/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/zigzag_full.png'
config_file  = r"/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/ibrahim_find_starting_node_config.wf" #config file 
launch_point = (34.02675, -81.2253)

option = 2
data = open_image(path_to_skel) # for option 2 
name = 'test.csv'
path_to_csv = write_chinese_post_man_csv(data, option, name)


circuit, graph = chinese_post_man(path_to_skel,config_file,launch_point, path_to_csv)

# print solution route
for e in circuit:
    print(e)

# print solution summary stats
for k, v in calculate_postman_solution_stats(circuit).items():
    print(k, v)