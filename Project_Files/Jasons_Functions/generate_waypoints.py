#!/usr/bin/env python

import numpy as np
import sys
import re
import cv2 as cv
import pandas as pd
import math
import os

from convert_coordinates import *

'''
NOTE: all tests and experiments are in the test_generate_waypoints.py
'''

def generate_waypoints(input_xy_coord_file, config_file, option="m"):
    '''
    generate_waypoints function that takes input file of xy coordinates
    and translates them into lat long

    Parameters
    ----------
    input_xy_coord_file, config_file, option
    option = m (stands for mission palnner) or c (csv file)

    Return
    ------
    output: no return but creates file with _waypoints.txt or .csv format
    '''

    mission_file_name = os.path.splitext(input_xy_coord_file)[0] + '_waypoints.txt'
    if option == "c":
        mission_file_name = os.path.splitext(input_xy_coord_file)[0] + '_waypoints.csv'
    print(mission_file_name)
    mission_file = open(mission_file_name, "w")

    if option == "c":
        mission_file.write("latitude,longitude,name,color\n")
    else:
        mission_file.write("QGC WPL 110\n")
    cnt = 0
    with open(input_xy_coord_file) as point_file:
        line = point_file.readline()
        while line:
            a = line.strip()
            x, y = a.split(',')
            line =point_file.readline()

            #FIXME: the config_file shouldn't always be oppened
            (LAT, LONG) = convert_xy_to_latlong(int(x),int(y), config_file)
            # print(LAT, LONG)
            if option == "m":
                out_line = str(cnt) + "\t" + str(1 if cnt==0 else 0)+ "\t" + str(0 if cnt==0 else 3) + "\t16\t"
                out_line += str(0.0) +"\t" + str(0.0) + "\t" +str(0.0) + "\t" + str(0.0) + "\t"
                out_line += str(LAT) + "\t" + str(LONG) + "\t" + str(111.0 if cnt==0 else 100.0) + "\t"
                out_line += str(1) + "\r"
                cnt +=1
            else:
                out_line = str(LAT) + "," + str(LONG) + ",," + "#FFF00" + "\n"

            mission_file.write(out_line)

def make_waypoint_file(input_file, option):
    """
    This will create a waypoint file in mission or csv format from input file

    Parameters
    ----------
        input file: filename in .csv format and containg Lattitude and Longitude columns
        option: type of generating file (m or c)

    Returns
    -------
        Output: waypoint file either with _watpoints.csv or mission _watpoints.txt format
    """
    out_dir = os.path.splitext(input_file)[0]
    mission_file_name = out_dir + '_waypoints.txt'
    print( "Location is in "  +out_dir + "\n")
    if option == "c":
        mission_file_name = os.path.splitext(input_file)[0] + '_waypoints.csv'
    print(mission_file_name)
    mission_file = open(mission_file_name, 'w')

    if option == "c":
        mission_file.write("latitude,longitude,name,color\n")
    else:
        mission_file.write("QGC WPL 110\n")
    cnt = 0

    df = pd.read_csv(input_file)
    for index, row in df.iterrows():
         #FIXME: the config_file shouldn't always be oppened
         (LAT, LONG) = (row['Latitude'], row['Longitude'])
         print(LAT, LONG)
         if option == "m":
             out_line = str(cnt) + "\t" + str(1 if cnt==0 else 0)+ "\t" + str(0 if cnt==0 else 3) + "\t16\t"
             out_line += str(0.0) +"\t" + str(0.0) + "\t" +str(0.0) + "\t" + str(0.0) + "\t"
             out_line += str(LAT) + "\t" + str(LONG) + "\t" + str(111.0 if cnt==0 else 100.0) + "\t"
             out_line += str(1) + "\r"
             cnt +=1
         else:
             out_line = str(LAT) + "," + str(LONG) + ",," + "#FFF00" + "\n"

         mission_file.write(out_line)

