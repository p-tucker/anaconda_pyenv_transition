# Create a venv

import subprocess
#import os
import venv
from pathlib import Path
from tkinter import Tk
from tkinter import filedialog

def create_venv(environment_name):
    # initiating environment creation if requested
    print(f"\nDo you have a backup file to use to build your virtual environment?")
    print("Enter 1 to select the file")
    print("Enter 2 to create a blank environment")
    print("Enter anything else to return to the main menu")
    environment_confirmation = input('Entry: ')
    if environment_confirmation == '1':
        print("Select the file to use as the restore point.")
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = filedialog.askopenfilename()
        print("You will be prompted to select a folder to save the virtual environment")  
        activate = input("Enter 1 to do so or anything else to return to the main menu. ")
        if activate == '1':
            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            folder_path = filedialog.askdirectory() # show an "Open" dialog box and return the path to the selected file
            print(f"Starting venv at {folder_path}")
            print("\nCreating Environment")
            venv.create(folder_path)
            print("\nActivating the environment")
            activation_code = ".venv\\Scripts\\activate"
            subprocess.run([activation_code])
            print("\nAdding dependencies")
            restore_code = "py -m pip install -r requirements.txt"
            subprocess.run([restore_code])
            print("------------------------------------")
        else:
            print("No Environment Created")
            print("Returning to the main menu")
            print("------------------------------------")

environment_name = "base"
create_venv(environment_name)