import sys, os
sys.path.append(os.path.join(sys.path[0],'Jasons_Functions'))

from zig_zag_pipeline import *

path_to_bw_boundaries = r'./MAPS/Map_originals/Ibrahim_Test/ibrahim_test_bw.png'

path_to_config_file = r'./MAPS/Map_originals/Ibrahim_Test/Ibrahim_test_config.wf'

launch_point = (34.02675, -81.2253)


zig_zag_pipeline(path_to_bw_boundaries,path_to_config_file,launch_point)