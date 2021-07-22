def get_negative_image(image):
    """takes in image and returns the negative of it 
        
    :param image: integer array of image
    :type image: integer array
    
    :rtype: integer array
    :return:  negative of image integer array
    """
    image = (255 - image)
    return image
