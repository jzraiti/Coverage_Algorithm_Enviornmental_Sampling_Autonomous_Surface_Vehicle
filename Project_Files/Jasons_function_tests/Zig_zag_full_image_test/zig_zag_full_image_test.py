import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from zig_zag_full_image import * #inputs: start_point,end_point,zig_zag_size,zig_zag_image,boundary_image, i

from open_or_show_image import * 


path_to_skeleton = r'./MAPS/Map_Skeletons/Ibrahim_test_skeletons/preprocessing/trimmed/trimmed_e4_d4___MAPS_Map_originals_Ibrahim_Test_ibrahim_test_bw_png_png_skeleton_lee94_png.png' 

path_to_boundary_image = r'./overlay_boundary_image.png'

zig_zag_width = 7

image = zig_zag_full_image ( path_to_skeleton, path_to_boundary_image, zig_zag_width) 

show_image(image)
cv2.imwrite('zigzag_full.png', image )


