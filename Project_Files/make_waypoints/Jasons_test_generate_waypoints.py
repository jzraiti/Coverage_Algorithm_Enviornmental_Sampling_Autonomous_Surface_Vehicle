#!/usr/bin/env python

import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")
from generate_waypoints import *

input_dir = "/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/make_waypoints/" #path to line_pttrn, config_file_line, out_file_type
line_pttrn = "Jasons_outfile.txt" # coordinate file 
config_file_line = "Jasons_Test_config.wf" #config file 

out_file_type = "m" #option = m (stands for mission palnner) or c (csv file)
# out_file_type = "c"

generate_waypoints(input_dir + line_pttrn, input_dir + config_file_line, out_file_type)




