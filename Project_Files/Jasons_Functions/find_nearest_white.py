import numpy as np

def find_nearest_white(img, target):
    """takes in image and target pixel and calculates closes white pixel to target
        
    :param img: integer array of image
    :type img: integer array
    :param target: coordinates of target pixel
    :type target: integer np array
    
    :rtype: float
    :return: distance between target and nearest white pixel
    """
    nonzero = np.argwhere(img == 255)
    distances = np.sqrt((nonzero[:,0] - target[0]) ** 2 + (nonzero[:,1] - target[1]) ** 2)
    nearest_index = np.argmin(distances)
    return nonzero[nearest_index]
