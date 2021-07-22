import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from zig_zag_full_image_2 import *

from open_or_show_image import * 


path_to_skeleton = r'./pipelines/zig_zag_skeleton.png' 

path_to_boundary_image = r'./Zig_zag_full_image_test_2/test_all_boundaries.png'

zig_zag_width = 8

image = zig_zag_full_image_2 ( path_to_skeleton, path_to_boundary_image, zig_zag_width) 

show_image(image)
cv2.imwrite('zigzag_full.png', image )




