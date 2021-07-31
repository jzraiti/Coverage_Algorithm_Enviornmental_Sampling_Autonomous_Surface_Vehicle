import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from zig_zag_full_image_3 import * 

from open_or_show_image import * 

path_to_skeleton = path_to_here + r'/zig_zag_skeleton.png' 

path_to_boundary_image = path_to_here + r'/test_all_boundaries.png'

zig_zag_width = 8

image,zig_zag_points_dict = zig_zag_full_image_3 ( path_to_skeleton, path_to_boundary_image, zig_zag_width) 

show_image(image)

cv2.imwrite('zigzag_full.png', image )

# print(zig_zag_points_dict)


