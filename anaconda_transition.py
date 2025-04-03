# This program will export an environment file from Anaconda
# it gives the user an option of doing a full backup of all packages currently in anaconda
# or doing it based on an individual environment
# It will then format the file into one that preserves the package name and version
# It will then configure a virtual environment using venv (if requested)

# this was written fast to accomodate the transition from anaconda to pyenv/venv
# please feel free to ask for changes

# things to take note of:
# this does not install python
# if you need a specific version of python you will need to install that using
# pyenv install <version>

# Patrick Tucker

import itertools
import subprocess
import os
import venv
from pathlib import Path
from tkinter import Tk
from tkinter import filedialog

#-----------------------------------------------------------------------------------------------------
def full_export():
    export_code = "conda list -e > anaconda_all_packages.txt"
    print("Running the following command:")
    print(export_code)
    #subprocess.run([export_code])
    #get_export = subprocess.run([export_code])
    username = os.getlogin()
    environment_name = "base"
    file_path = Path(f"C:\\Users\\{username}\\anaconda_all_packages.txt")
    if file_path.exists():
        print(f"File '{file_path}' exists.")
        print("------------------------------------")
        file_conversion(environment_name,file_path)
    else:
        print(f"File '{file_path}' does not exist.")
        print("------------------------------------")

#-----------------------------------------------------------------------------------------------------
def named_export():
    environment_name = input("What is the environment name to export? ")
    print("Running the following command:")
    export_code = "conda list --name " + environment_name +" --export > " + environment_name+"_export.txt"
    print(export_code)
    #subprocess.run([export_code])
    #get_export = subprocess.run([export_code])
    username = os.getlogin()
    file_path = Path(f"C:\\Users\\{username}\\{environment_name}_export.txt")
        
    if file_path.exists():
        print(f"File '{file_path}' exists.")
        print("------------------------------------")
        print("File Output:")
        
        # calling the file conversion function
        file_conversion(environment_name, file_path)
        print("File converted")
        print("------------------------------------")
        
    else:
        print(f"File '{file_path}' does not exist.")
        print("Please verify you typed the environment name correctly.")
        print("Returning to the main menu.")
        print("------------------------------------")


#-----------------------------------------------------------------------------------------------------
# Convert the exported file into one that venv can use
def file_conversion(environment_name,file_name):
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
            new_file = open(f"C:\\Users\\{username}\\{environment_name}_export_update.txt", "a")
            new_file.write(data_line)
            new_file.write('\n')
            new_file.close()

#-----------------------------------------------------------------------------------------------------
# Create venv
def create_venv(environment_name):
    # initiating environment creation if requested
    print(f"\nDo you have a backup file to use to build your virtual environment?")
    print("Enter 1 to select the file")
    print("Enter 2 to create a blank environment")
    print("Enter anything else to return to the main menu")
    environment_confirmation = input('Entry: ')
    if environment_confirmation == '1':
        print("You will be prompted to select a folder to save the virtual environment")  
        activate = input("Enter 1 to do so or anything else to return to the main menu. ")
        if activate == '1':
            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            folder_path = filedialog.askdirectory() # show an "Open" dialog box and return the path to the selected file
            print(f"Starting venv at {folder_path}")
            venv.create(folder_path)
            print("Creating Environment")
            print("------------------------------------")
        else:
            print("No Environment Created")
            print("Returning to the main menu")
            print("------------------------------------")

#-----------------------------------------------------------------------------------------------------
# Add new Python versions
# This is not being used.
'''
def pyenv_caller():
    continue_loop = True
    while continue_loop:
        pyversion = input("What version of python do you need installed?")
        pyscript = f"pyenv install {pyversion}"
        subprocess.run([pyscript])
        print("Here are the versions you currently have installed: ")
        subprocess.run("pyenv versions")
        print("This program is not configured to remove any versions")
        more_versions = input("Enter 1 to add more versions. Any other key will exit.")
        if more_versions != 1:
            continue_loop = False
'''

#-----------------------------------------------------------------------------------------------------
def main_program():
    continue_loop = True
    while continue_loop: 
        print("\nDo you need to perform a full export, named export, or set up a new environment?" )
        print("1 for full backup from Anaconda")
        print("2 for named environment that already exists in Anaconda")
        print("3 for a new virtual environment using Venv")
        #print("Type \'python\' to install a specific version of python")
        determine_backup = input("or any other key to quit. ")
        print("------------------------------------")
        if determine_backup == '1':
            full_export()
        elif determine_backup == '2':
            named_export()
        elif determine_backup =='3':
            venv_name = input("What is your environments name?")
            create_venv(venv_name)
        #elif determine_backup.upper() == 'PYTHON':
            # not going to do this anymore
            # print("Lets get you a new version of python using pyenv.")
            # pyenv_caller()
        else:
            continue_loop = False

#-----------------------------------------------------------------------------------------------------


main_program()



