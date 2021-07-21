import numpy as np
from shapely.geometry import LineString

def find_line_segment_intersection(line1,line2):
    """takes in two lines and outputs location of their intersection
    
    :param line1: array of two points
    :type line1: integer array
    :param line2: array of two points
    :type line2: integer array
    
    :rtype: int array
    :return: location of intersection
    """
    line1 = LineString([(line1[0][0],line1[0][1]) , (line1[1][0],line1[1][1] )])
    line2 = LineString([(line2[0][0],line2[0][1]) , (line2[1][0],line2[1][1] )])

    intersection = np.array( [ int( line1.intersection(line2).x ) , int( line1.intersection(line2).y ) ] )

    return intersection