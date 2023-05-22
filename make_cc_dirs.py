#! python3
import os

days = ["day_1", "day_2", "day_3", "day_4", "day_5", "weekend"] 
num_of_dirs = int(input("Input number of weekly directories to populate: "))
base_dir = input("Input base directory: ")

week_start = 1
while week_start <= num_of_dirs:
    if week_start < 10:
        week_start_str = "week0" + str(week_start)
    if week_start > 9:
        week_start_str = "week" + str(week_start)


    week_dir = os.path.join(base_dir, week_start_str)
    
    try:
        os.mkdir(week_dir)
    except FileExistsError:
        print(week_dir + " already exists")

    current_week = base_dir + week_start_str
    
    for day in days:
        day_dir =  os.path.join(current_week, day)
        try:
            os.mkdir(day_dir)
        except FileExistsError:
            print(day_dir + " already exists")

    week_start += 1


# Use os.mkdirs in loop to populate current_week path with directories

# Set up loop to increment week_start and cycle through week directories, and implement make directories.

