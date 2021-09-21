import sys, os
sys.path.append(os.path.join(sys.path[0],'Jasons_Functions'))

#print(sys.path[0])


from zig_zag_pipeline import *

print("\n\n" + sys.path[0] + "\n\n")

path_to_bw_boundaries = sys.path[0] + r'/Jason_Sept_16_inputs/exp1_sept_2021_out_cleaned.png'

path_to_config_file = sys.path[0] + r'/Jason_Sept_16_inputs/Sept_exp1_2021.wf'

launch_point = (   34.02618   ,  -81.2358  )

print("Reminder: there are multiple arbitrary values inside of the zig zag pipline function which are hardcoded presently")
zig_zag_pipeline(path_to_bw_boundaries,path_to_config_file,launch_point)