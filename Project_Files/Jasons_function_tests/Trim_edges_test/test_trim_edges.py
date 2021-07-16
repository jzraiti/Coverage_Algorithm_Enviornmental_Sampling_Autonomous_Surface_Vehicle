import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from trim_edges import * # new_array = trim_edges(path,weight_threshold)
from open_or_show_image import *


path = r'./MAPS/Map_originals/Ibrahim_Test/e4_d4_image.png' 
weight_threshold = 30

new_array , new_image =trim_edges(path,weight_threshold)

show_image(new_image)