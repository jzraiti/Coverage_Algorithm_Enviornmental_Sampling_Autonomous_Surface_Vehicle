# Python program to explain cv2.line() method

# importing cv2
import cv2

#import matplotlib for plotting since cv2 doesnt seem to want to do that
import matplotlib.pyplot as plt
# path
path = r'/home/jasonraiti/Documents/GitHub/USC_REU/OpenCV_tests/test.png'

# Reading an image in grayscale mode
image = cv2.imread(path, 0)

if image is None:
    print("Check file path")

# Window name in which image is displayed
window_name = 'Image'

# Start coordinate, here (225, 0) tuple
# represents the top right corner of image
start_point = (0, 100)

# End coordinate, here (0, 225)
# represents the bottom left corner of image
end_point = (225, 225)

# Black color in BGR
color = (0, 0, 0)

# Line thickness of 5 px
thickness = 1

# Using cv2.line() method
# Draw a diagonal black line with thickness of 5 px
image = cv2.line(image, start_point, end_point, color, thickness)

# Displaying the image
#cv2.imshow(window_name, image) THIS SHIT DONT WORK 

#plot with matplt.lib instead
plt.imshow(image, cmap='gray')
plt.show()

print("done")