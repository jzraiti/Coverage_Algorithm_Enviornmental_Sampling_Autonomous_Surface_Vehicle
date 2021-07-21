import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from find_line_segment_intersection import *

from open_or_show_image import *

from drawline import *

# path to images
path1 = r'./MAPS/Map_originals/Lake_Murray_Map_Originals/e_d_image4.png'

#original image
image1 = open_image(path1)

# define edge boundaries 
top_side = [(1,1) , (1,image1.shape[1] -1 )]
bottom_side = [(image1.shape[0] -1,image1.shape[1] -1) , (image1.shape[0]-1 ,1) ]
right_side = [(1 ,image1.shape[1] - 1) , (image1.shape[0]-1,image1.shape[1]-1)]
left_side = [(image1.shape[0]-1,1) , (1,1)]

#find intersection
intersection1 = find_line_segment_intersection(bottom_side,right_side)
intersection2 = find_line_segment_intersection(top_side,left_side)
print(intersection1,intersection2)

#create black canvas
black_image = np.zeros((image1.shape[0],image1.shape[1])) # get black background 
new_image = black_image

#drawline
new_image = drawline(intersection1 , intersection2 , black_image)

# print(new_image)

show_image(new_image)
for i in new_image:
    for j in i:
        if j > 0 :
            print('we good')
            break