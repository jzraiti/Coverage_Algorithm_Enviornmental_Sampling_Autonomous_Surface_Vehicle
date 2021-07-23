
import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from overlay_images import *



path1 = r'./pipelines/overlay_boundary_image.png'

path2 = r'./pipelines/zig_zag_skeleton.png' 

image1 = open_image(path1)

image2 = open_image(path2)

make_negative_1 = False
make_negative_2 = True

new_image = overlay_images (image1,image2,make_negative_1, make_negative_2)

show_image(new_image)
cv2.imwrite('test_all_boundaries.png', new_image*255 )
