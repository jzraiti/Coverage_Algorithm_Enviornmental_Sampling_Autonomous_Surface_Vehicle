import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from write_chinese_post_man_csv import *
from open_or_show_image import * 


# option = 1 
# data = r'./write_chinese_post_man_csv_test/zigzag_full.png'
# name = 'test.csv'

option = 2
data = r'./write_chinese_post_man_csv_test/zigzag_full.png'
data = open_image(data) # for option 2 
name = 'test.csv'

path_to_csv = write_chinese_post_man_csv(data, option, name)

print(path_to_csv)