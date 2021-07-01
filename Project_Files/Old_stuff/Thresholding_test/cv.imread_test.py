import cv2 as cv
import sys

#finds the file called lake.jpg
img = cv.imread(cv.samples.findFile("lake.jpg"))


if img is None:
    sys.exit("Could not read the image.")

#displays image called lake.jpg (suprised this part works...)
cv.imshow("Display window", img)

#we want program to wait until user presses key
# 0 = wait forever
# 10 *1000 = wait for 10 seconds (measured in milliseconds)
k = cv.waitKey(10*1000)

#write new image to png
if k == ord("s"):
    cv.imwrite("lake_png.png", img)
