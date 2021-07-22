
import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from overlay_images import *



path1 = r'./MAPS/Map_originals/Ibrahim_Test/e4_d4_image.png'

path2 = r'./_d1e0___inverse_skeletons_e1_d0_negative_skeleton_png_png_medial_axis_png.png' 

image1 = open_image(path1)

image2 = open_image(path2)

make_negative_1 = False
make_negative_2 = True

new_image = overlay_images (image1,image2,make_negative_1, make_negative_2)

show_image(new_image)
