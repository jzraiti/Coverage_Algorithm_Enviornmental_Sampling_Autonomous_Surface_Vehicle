# A Novel Algorithmic Coverage Method for Environment Sampling with an Autonomous Surface Vehicle

## What is this:
A novel coverage/path-creation algorithm for marine enviornmental sampling using an Autonomous Surface Vehicle

This algorithm uses skeletonization and a modified boustrophedon method to cover large areas and tight spaces equitably 

## How to use this program:

#### To create zigzag from skeleton path:

1. take an satellite image of an operation area
    - ![Alt text](Project_Files/MAPS/Map_originals/Ibrahim_Test/ibrahim_test.png?raw=true "Lake Murray - Ibrahim test area")
2. manually threshold the image so that the navigable water is white and the boundary is black
    - ![Alt text](Project_Files/MAPS/Map_originals/Ibrahim_Test/ibrahim_test_bw.png?raw=true )
3. create config file in the proper format
    - see : Project_Files/MAPS/Map_originals/Ibrahim_Test/Ibrahim_test_config.wf
4. locate the latitude and longitude of your launch point
    - Jakes landing for this example: (34.02675, -81.2253)
5. Plug these values into Project_Files/zig_zag_pipeline_test.py
6. Outputs you will get:
    - coordinates_waypoints.csv
        - waypoints in order of travel
    - coordinates_waypoints.txt
        - mission file for use by jetyak
    - zigzag_full 
        - image of the path to be taken
    - ![Alt text](Project_Files/MAPS/Map_outputs/Ibrahim_test/Pipeline_july27/zigzag_full.png?raw=true )


#### To create a circular path around skeleton:
modify the script in Project_Files/Jupyter_pipelines/Pipeline_Circle_Path_Jul30
    - ![Alt text](Project_Files/MAPS/Map_outputs/Ibrahim_test/Pipeline_Circle_Path_Jul30/e_d_image.png?raw=true )
    - ![Alt text](Project_Files/MAPS/Map_outputs/Ibrahim_test/Pipeline_Circle_Path_Jul30/pixelremoved_thinned_circle_skeleton.png?raw=true )



## Parameters that can be tweaked inside of the code:

- from Jasons_Functions/zig_zag_pipeline.py : 
    - weight_threshold for trim_edges steps = 42
    - which skeleton to use [med_axis , skeleton , skeleton_lee , thinned] = skeleton_lee
    - which skeleton of skeleton to use [med_axis , skeleton , skeleton_lee , thinned] = medial axis
    - zig_zag_width (number of pixels in the base of each triangle)= 8




## File Structure:
- Project files
    - Jasons_function_tests: 
        - *these are scripts that test the functions in jasons_functions*
        - *the sys path will need to be modified for them to work, add path to jasons_functions*
    - Jasons_Functions: tring explaining inputs and outputs and purpose*
        - zig_zag_pipeline.py
            - *this is the main function which will run the complete image to waypoints pipeline*
    - Jasons_old_scripts:
        - *previous iterations of programs, retained just in case something breaks or a previous method is needed*
    - Jupyter_pipelines
        - *these are jupyter notebooks that implement the coverage patterns*
        - *the paths in these are going to need to be edited as currently they are specific to the lab computer*
        - Pipeline_Circle_Path_Jul30
            - *this creates a circlular path around the skeleton for ibrahim test area*
        - Pipeline_july27
            - *this creates a zig zag path for ibrahim test area*
            - *total length of path (in meters) is 6891.998172156519, max distance:  69.87131027825369 , mean distance:  7.5632924271105475*
    - MAPS
        - Map_originals
            - *contains the starting data for various bodies of water*
            - Ibrahim_test
                - *a small corner of lake murray in the south eastern corner by jakes landing*
        - Map_Skeletons
            - *contains the skeletonized images for various bodies of water*
        - Map_outputs
            - *contains the outputs of iterations of coverage algorithms*
- specific_requirements.txt
    - *all packages used in this program (so far as I know)*
    - *python == 3.8.5*
- all_possible_requirements.txt
    - *apologies for the messy virtual enviornment*


## Special thanks to:
https://github.com/AutonomousFieldRoboticsLab/coverage_path_planning
https://github.com/brooksandrew/postman_problems#python

## Future work:

resolve pathing to functions and images and config files for users not on the lab computer

double check requirements file 

give user direct control over the arbitrary parameters

automate the thresholding manual preprocessing step

add function to create the config file for the user automatically

add boustrophedon coverage method for comparison 

make the reasource constraints a part of the inputs (time or distance to travel in meters)
