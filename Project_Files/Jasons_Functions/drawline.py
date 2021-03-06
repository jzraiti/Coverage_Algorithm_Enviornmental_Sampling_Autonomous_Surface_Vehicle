import cv2

#this function draws a line between two points on an image array (note image arrays are indexed weird)
def drawline(p1,p2,image):
    """takes in two np array points and an image to draw on, spits out the image with a line between points 
        
    :param p1: integer array of a point
    :type p1: integer numpy array
    :param image: WHITE ON BLACK image 
    :type iamge: integer np array
    
    :rtype: integer np array
    :return: image w a line between points 
    """
    p1 = tuple(p1.astype(int).tolist()) #input is numpyfloat array
    p2 = tuple(p2.astype(int).tolist()) # cv2.line needs tuple int inputs 
    color = (255, 255, 255) # color in BGR
    thickness = 1 # line thickness  

    #AND THEN FLIP THE  Y , X  FORMAT TO GRAPH IT CORRECTLY !!!!!! 
    start_point  = [p1[1],p1[0]]
    end_point = [p2[1],p2[0]]

    return(cv2.line(image, start_point, end_point, color, thickness))