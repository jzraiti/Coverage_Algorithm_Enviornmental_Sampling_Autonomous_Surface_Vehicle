import cv2 

# import sys
# sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from jasons_skeletonize_from_array import * 

from trim_edges import * # new_array = trim_edges(path,weight_threshold)

from erosion_dilation_from_array import *

from inverse_skeletonize_from_array import *

from overlay_images import *

from zig_zag_full_image_3 import *

from write_chinese_post_man_from_graph_csv import *

from chinese_post_man_from_graph import *

from find_coverage_metrics_from_array import *

from get_graph_distance import *

from find_coverage_metrics_from_array import *

from generate_waypoints import *




def zig_zag_pipeline(path_to_bw_boundaries,path_to_config_file,launch_point_lat_long):
# def zig_zag_pipeline():
    '''
    inputs: path_to_bw_boundaries,path_to_config_file,launch_point_lat_long
    
    some arbitrary settings to pay attention to: 
    weight_threshold for trim_edges steps = 42
    which skeleton to use [med_axis , skeleton , skeleton_lee , thinned] = skeleton_lee
    which skeleton of skeleton to use [med_axis , skeleton , skeleton_lee , thinned] = medial axis
    zig_zag_width (number of pixels in the base of each triangle)= 8

    
        
    '''
    # erosion dilation -----------------------------------------------------------------------
    # WARNING : important edge case is when your skeleton has a loop in it, this may mess up all of the algorithms pretty bad 

    # path to image
    path = path_to_bw_boundaries
    config_file = path_to_config_file
    launch_point = launch_point_lat_long # for jakes landing (34.02675, -81.2253)


    
    
    image = open_image(path)
    option = 2 # 1 = erode first 2 = dialate first 
    num_erosions = 4
    num_dilations = 4

    e_d_image  = erosion_dilation_from_array(image,option,num_erosions,num_dilations)

    cv2.imwrite('e_d_image.png', e_d_image)

    # skeletonize 
    med_axis , skeleton , skeleton_lee , thinned , thinned_partial = jasons_skeletonize_from_array(e_d_image)

    skeletons = [med_axis , skeleton , skeleton_lee , thinned]

    #try and preprocess the skeletons a bit and trim edges ---------------------------------------------------
    trimmed_skeletons = []
    # arbitrary value alert!!!! *************************************************
    weight_threshold = 42 # this is one of those 
    for skel in skeletons:

        cv2.imwrite('temp_skel_img.png', skel)

        new_array , new_image = trim_edges('temp_skel_img.png',weight_threshold)
        trimmed_skeletons.append(new_image)
        
        

    #inverse skeletonize trimmed graphs ---------------------------------------------------------------------

    lotsa_inverse_skeletons = []
    for trim_skel in trimmed_skeletons:


        med_axis , skeleton , skeleton_lee , thinned , thinned_partial = inverse_skeletonize_from_array(trim_skel)

        inverse_skeletons = [med_axis , skeleton , skeleton_lee , thinned]

        lotsa_inverse_skeletons.append(inverse_skeletons)
        

    #overlay boundary and one inverse skeleton image ----------------------------------------------------------------
    #this is where one of the skeletons is chosen to be used

    image1 = e_d_image
    # arbitrary value alert!!!! *************************************************
    image2 = (lotsa_inverse_skeletons[3][0]>0)*255 # grab skeleton lee, medial axis 
    # show_image(image1)
    # show_image(image2)
    cv2.imwrite( "medial_axis_inverse_skeleton.png", image2*255 )

    make_negative_1 = False
    make_negative_2 = True

    new_image = overlay_images (image1,image2,make_negative_1, make_negative_2)
    # show_image(new_image)

    #combine boundary and skeleton images to create full boundary image --------------------------------------------
    image1 = new_image
    image2 = trimmed_skeletons[3] 

    # show_image(image1)
    # show_image(image2)

    make_negative_1 = False
    make_negative_2 = True

    new_image = overlay_images (image1,image2,make_negative_1, make_negative_2) #Error checking notes: seems to work good up to this point

    # show_image(new_image)

    skel_name = 'zig_zag_skeleton.png'
    bound_name = 'overlay_boundary_image.png'

    cv2.imwrite( skel_name, trimmed_skeletons[3] )
    cv2.imwrite( bound_name, new_image*255 )


    #create full zig zag, this time with modified zig zag that prevents overlapping paths ---------------------------------------------------------

    path_to_skeleton = skel_name

    path_to_boundary_image = bound_name

    # arbitrary value alert!!!! *************************************************
    zig_zag_width = 16 #used to be 8 but this should speed things up

    image,zig_zag_points_dict = zig_zag_full_image_3 ( path_to_skeleton, path_to_boundary_image, zig_zag_width) 

    # show_image(image)

    zig_zag_name = 'zigzag_full.png'

    cv2.imwrite(zig_zag_name, image )

    #create csv file from zig zag full --------------------------------------------------------------------------------------------------------------------

    # arbitrary value alert!!!! *************************************************
    lee_skel = trimmed_skeletons[3]
    name = 'trim_skel_graph.csv'

    graph = skeleton_to_graph_from_array(lee_skel)

    path_to_csv = write_chinese_post_man_from_graph_csv(graph,name)
    # print(path_to_csv)


    #use chinese post man to calculate most efficient route covering all edges ---------------------------------------------------------------------------------------
    #HEADS UP : you will need to make a custom config file for each map you apply this to , as well as pick some arbitrary launch point (jakes landing )
    # PRAISE BE TO https://github.com/brooksandrew/postman_problems#python where i got the bones for this code from

    #inputs
    # path_to_skel = zig_zag_name
    #get path_to_csv from  write_cpp_from_graph_csv2(graph,name)
    lee_skel = trimmed_skeletons[3]
    graph = skeleton_to_graph_from_array(lee_skel)

    # config_file  = r"/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Pipeline_july27/ibrahim_config.wf" #config file 
    # arbitrary value alert!!!! *************************************************
    # launch_point = (34.02675, -81.2253)

    circuit, graph = chinese_post_man_from_graph(graph,config_file,launch_point, path_to_csv)

    #calulate the distance in meters of your graph -----------------------------------------------------------------------------------------------------------------
    path = zig_zag_name

    #take 2 arbitrary points 
    waypoint1 = convert_xy_to_latlong(0, 0, config_file)
    waypoint2 = convert_xy_to_latlong(0, 1, config_file)

    #use those points to calculate distance ---- this could be streamlined by getting the arbitrary points inside get_graph_distance later 
    total_distance, weight_sum , unit_distance = get_graph_distance(waypoint1,waypoint2,path)
    print("total distance (meters) : " , total_distance )

    # Calculate MEAN DISTANCE TO SAMPLED POINT as well--------------------------------------------------------------------------------------------------------------

    boundary_path = r'e_d_image.png' # can get these from earlier in the code instead 
    zig_zag_path = r'zigzag_full.png'
    boundary = open_image(boundary_path)
    zig_zag = open_image(zig_zag_path) 
    # show_image(zig_zag)

    max_distance,mean_distance,points_sum,distance_sum,distance_graph = find_coverage_metrics_from_array (boundary,zig_zag)

    print("coverage metrics: \n max distance: ", max_distance,"mean distance: ", mean_distance)
    plt.imshow(distance_graph, cmap=plt.cm.jet)
    plt.savefig("heatmap.png")
    plt.show()


    #create file of x,y coordinate points in the order of cpp -----------------------------------------------------------------------------

    f = open("coordinates.txt", "w")
    # f.write()

    edges = graph.edges()
    # ps = graph[s][e]['pts']
    #graph[s][e]['pts']

    for e in circuit:
        node0 = int(e[0])
        node1 = int(e[1])
        
        points = zig_zag_points_dict.get( (node0,node1) )

        # if len(points) == 0: print('error at' , e)
        # else: print(points)
        
        for pt in range(0,len(points)):
            f.write(str(points[pt][1]) + ',' + str(points[pt][0]) + '\n') # convert from y,x format to x,y format 

        points = []

    f.close()

    #convert coordinates to waypoints -------------------------------------------------------------------------------------------

    # input_dir = "/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Pipeline_july27/" #path to line_pttrn, config_file_line, out_file_type
    input_dir = ""
    line_pttrn = "coordinates.txt" # coordinate file 
    config_file_line = config_file #config file 

    out_file_type = "c" #option = m (stands for mission palnner) or c (csv file)

    generate_waypoints(input_dir + line_pttrn, input_dir + config_file_line, out_file_type)

    out_file_type = "m" #option = m (stands for mission palnner) or c (csv file)

    generate_waypoints(input_dir + line_pttrn, input_dir + config_file_line, out_file_type)
    
    return 0