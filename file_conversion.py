# If you only need to convert your files you can run this script

import itertools
import os
from pathlib import Path
from tkinter import Tk
from tkinter import filedialog

print("Select a text file to convert")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file_name = filedialog.askopenfilename()
file_name_short = file_name[:-4]
#Open the file
username = os.getlogin()
print("Please be aware that this process will append to a file if it already exists.")
with open(file_name, 'r') as exported_file:
    #Iterate over each line after skipping the 3 header lines
    for line in itertools.islice(exported_file, 3, None):
        #Split each line by equals sign
        data = line.strip().split('=')
        data.pop()
        print(data)
        data_line = f"{data[0]} == {data[1]}"
        new_file = open(f"{file_name_short}_export_update.txt", "a")
        #new_file = open(f"C:\\Users\\{username}\\{file_name_short}_export_update.txt", "a")
        new_file.write(data_line)
        new_file.write('\n')
        new_file.close()