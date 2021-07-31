# A Novel Algorithmic Coverage Method for Environment Sampling with an Autonomous Surface Vehicle




## What is this:




## How to use this program:




## Parameters that can be tweaked inside of the code:

from Jasons_Functions/zig_zag_pipeline.py : 
weight_threshold for trim_edges steps = 42
which skeleton to use [med_axis , skeleton , skeleton_lee , thinned] = skeleton_lee
which skeleton of skeleton to use [med_axis , skeleton , skeleton_lee , thinned] = medial axis
zig_zag_width (number of pixels in the base of each triangle)= 8




## File Structure:
-Project files
    -Jasons_function_tests: 
        -*these are scripts that test the functions in jasons_functions*
        -*the sys path will need to be modified for them to work, add path to jasons_functions*
    -Jasons_Functions:
        *these are all of the functions that are used by the program, or can be used by futureprograms, in each function there is a docstring explaining inputs and outputs and purpose*
        zig_zag_pipeline.py
            *this is the main function which will run the complete image to waypoints pipeline*
    Jasons_old_scripts:
        *previous iterations of programs, retained just in case something breaks or a previous method is needed*
    Jupyter_pipelines
        *these are jupyter notebooks that implement the coverage patterns*
        *the paths in these are going to need to be edited as currently they are specific to the lab computer*
        Pipeline_Circle_Path_Jul30
            *this creates a circlular path around the skeleton for ibrahim test area*
        Pipeline_july27
            *this creates a zig zag path for ibrahim test area*
    MAPS
        Map_originals
            *contains the starting data for various bodies of water*
            Ibrahim_test
                *a small corner of lake murray in the south eastern corner by jakes landing*
        Map_Skeletons
            *contains the skeletonized images for various bodies of water*
        Map_outputs
            *contains the outputs of iterations of coverage algorithms*
specific_requirements.txt
    *all packages used in this program (so far as I know)*
    *python == 3.8.5*
all_possible_requirements.txt
    *apologies for the messy virtual enviornment*


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
