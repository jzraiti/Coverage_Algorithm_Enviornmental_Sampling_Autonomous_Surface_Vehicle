############################################
#   Author: Nare Karapetyan
#   Date: July 26 2018
#   
#   Comment: performs all conversions from xy to latlon and vise versa
#   - xy to lat lon
#   - lat lon to xy
#   - computes rsoltuon
#   - computs meter per pixel
############################################

import numpy as np
import sys
import re
import cv2 as cv
import math

#NOTE: Tests are in test_conversion.py

def get_world_information(config_file):
# CPP NOTE
    '''
	Input: configs file where information
	about bottom and top lat and long is given and image size
	Output: resoltution, upper and bottop LAT and LONG, 

         image_size, upper_long_lat, bottom_long_lat

	Method: Reads information from the file
    '''
    img_width = None
    img_height = None

    upper_long = None
    upper_long = None

    bottom_lat = None
    bottom_lat = None

    with open(config_file, 'rt') as in_file:
        for line in in_file:
            #if line.startswith("Upper"):# Left Lattitude"):
            if re.search(r'\bUpper Left Latitude\b', line):
                words = line.split(':')
                upper_lat = float(words[1])
            if re.search(r'\bUpper Left Longitude\b', line):
                words = line.split(':')
                upper_long = float(words[1])
            if re.search(r'\bBottom Right Latitude\b', line):
                words = line.split(':')
                bottom_lat = float(words[1])
            if re.search(r'\bBottom Right Longitude\b', line):
                words = line.split(':')
                bottom_long = float(words[1])

            if re.search(r'\bImage Width\b', line):
                words = line.split(':')
                img_width = float(words[1])
            if re.search(r'\bImage Height\b', line):
                words = line.split(':')
                img_height = float(words[1])

    image_size = (img_width, img_height)
    upper_long_lat = (upper_long, upper_lat)
    bottom_long_lat = (bottom_long, bottom_lat)

    return image_size, upper_long_lat, bottom_long_lat

def get_meter_per_pixel(config_file):

    metersPerPixel = None

    with open(config_file, 'rt') as in_file:
        for line in in_file:
            if re.search(r'\bMeters Per Pixel\b', line):
                words = line.split(':')
                metersPerPixel = float(words[1])
    return metersPerPixel

def get_resolution(config_file):

# CPP NOTE but not the relative size part

    image_size, upper_long_lat, bottom_long_lat = get_world_information(config_file)

    if(image_size[0] == None or image_size[1] == None):
        image_size = get_relative_image_size(upper_long_lat, bottom_long_lat)
    
    x_resolution = (-bottom_long_lat[0] + upper_long_lat[0]) / float(image_size[0])
    y_resolution = (-bottom_long_lat[1] + upper_long_lat[1]) / float(image_size[1])
    
    resolution = (x_resolution, y_resolution)
    return resolution

def convert_xy_to_latlong(x,y, config_file):
    '''
	Input: x y coordinates and config_file to calculate resolution
	Output: lat and longitude

	Method: Converts x y coordinates in image frame to lat and longitude
    '''

    #TODO: this part can be modified with introduction of a class and a common variables
    # so the f-n will not be always called
    image_size, upper_long_lat, bottom_long_lat = get_world_information(config_file)
    
    if(image_size[0] == None or image_size[1] == None):
        image_size = get_relative_image_size(upper_long_lat, bottom_long_lat)
    
    x_resolution = (- bottom_long_lat[0] + upper_long_lat[0]) / image_size[0]
    y_resolution = (- bottom_long_lat[1] + upper_long_lat[1]) / image_size[1]

    long_coord = upper_long_lat[0] - x_resolution * x
    lat_coord = upper_long_lat[1]  - y_resolution * y

    lat_long_coordinates = (lat_coord, long_coord)
    
    return lat_long_coordinates

def convert_xy_to_latlong_db(x, y, config_file):
    '''
    The way of lat lon is calculated in Dubin's coverage
    '''
    image_size, upper_long_lat, bottom_long_lat = get_world_information(config_file)
    
    meters_per_pixel = get_meter_per_pixel(config_file)

    lat_per_meter = 1.0/111111
    lon_per_meter = 1.0/(111111*math.cos(math.pi * upper_long_lat[1]/180.0))

    lat_per_pixel = meters_per_pixel * lat_per_meter
    lon_per_pixel = meters_per_pixel * lon_per_pixel
    
    long_coord = upper_long_lat[0] + lat_per_pixel * x
    lat_coord = upper_long_lat[1] + lat_per_pixel * y

    lat_long_coordinates = (lat_coord, long_coord)
    
    return lat_long_coordinates

def convert_latlong_to_xy(LONG, LAT, config_file):
    '''
    Input: LONG LAT and config file
    Output: x and y coordinates
    Method: converts LONG LAT to x y
    '''
    image_size, upper_long_lat, bottom_long_lat = get_world_information(config_file)
    resolution = get_resolution(config_file)

    '''test'''
    print('resolution:', resolution[0], resolution[1])
    print(' LONG, LAT: ', LONG, LAT)
    print(' upper LONGG, LAT: ', upper_long_lat[0], upper_long_lat[1])
    ''''''''''''''''''''''''''
    
    # xtemp = (- LONG + upper_long_lat[0])
    # ytemp =  (- LAT + upper_long_lat[1])
    # print("x long diff : ", xtemp )
    # print("y lat diff : ", ytemp )


    x_coord = (- LONG + upper_long_lat[0]) / resolution[0] # x resoltion #TODO: can replace resolution with dictionry and lookup for resolution['x']
    y_coord = (- LAT + upper_long_lat[1]) / resolution[1] # y_resoltuon

    xy_coordinates = (int((x_coord)), int((y_coord)))
    return xy_coordinates 

#NOTE: cartesaian coordiantes not image
def convert_latlong_to_xy_version2(LONG, LAT, config_file):
    image_size, upper_long_lat, bottom_long_lat = get_world_information(config_file)
    
    width = image_size[0]
    hight = image_size[1]

    x_coord = (width * (180+LONG)/360) % (width + (width/2))
    
    mercN = math.log(math.tan(math.pi/4.0) + (LAT * math.pi/90))
    y_coord = (hight /2) - (width * mercN/(2 * math.pi))
    
    return (int(y_coord), int(x_coord))


# FIXME:: need this??? added the check of image size if None then calculates the image
# Finds relative coordinates of points based on long lat
# Assumes that Upper long and lat are the (0,0)
# and bootm ones are used for finding the width and height of the area
def latlong_based_convert_xy_to_latlong(x, y, config_file):
    return latlong_coorindates


def get_relative_image_size(upper_long_lat, bottom_long_lat):

    #upper_long_lat and (upper_lat and bottom_long)
    width = find_distance(upper_long_lat, (bottom_long_lat[0], upper_long_lat[1]))
    #upper_long_lat and (bottom_lat and upper_long)
    height = find_distance(upper_long_lat, (upper_long_lat[0], bottom_long_lat[1]))

    return (int(width), int(height))


# Finds the distance in meters given two points in LONG and LAT
# CPP NOTE
def find_distance(upper_long_lat, bottom_long_lat):

    #converting to the radians
    upper_long = upper_long_lat[0] * math.pi/180.0
    upper_lat = upper_long_lat[1] * math.pi/180.0
    bottom_long = bottom_long_lat[0] * math.pi/180.0
    bottom_lat = bottom_long_lat[1] * math.pi/180.0

    #haversine Formulat
    dist_long = bottom_long - upper_long
    dist_lat = bottom_lat - upper_lat
    distance = pow(math.sin(dist_lat / 2.0), 2) + math.cos(upper_lat)*math.cos(bottom_lat)*pow(math.sin(dist_long/2.0),2)

    distance = 2 * math.asin(math.sqrt(distance))

    #Radius of Earth in Kilometers
    #for miles R = 3956
    R = 6371.0

    distance = distance*R

    #converts into meters
    return distance* 1000.0
