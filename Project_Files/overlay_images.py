    
    
    
    
    
    
    
    
    
    
    
    
    
    """makes a full zig zag image ready to be used for traveling salesman solution and then conversion to coordinate points/mission plan
    
    #inputs: path1 path2 , make image 1 negative, make image 2 negative
    #note only works with making images with a white background

    
    :param path_to_skeleton: full path to a preprocessed skeleton
    :type path_to_skeleton: str
    :param path_to_boundary_image: full path to preprocessed boundaries image
    :type path_to_boundary_image: str
    :param: desired zig_zag_width (in pixels)
    :type: int
    
    :rtype: integer numpy array
    :return:  a black background white forground image of just the zig zag path (full)
    """