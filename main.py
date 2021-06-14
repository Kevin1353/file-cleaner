# Import required modules
import os

# The following path determines the folder we will be cleaning up
path = "C:/Users/kev12/Downloads/02_Classwork_2020_Networks1.docx"


# this gets the individual file that we will be using
def get_file():
    os.listdir(path)  # this lists all files in a directory


# this finds the time of a file
age = os.stat(path)

# this removes a specific file
# os.remove("C:/Users/kev12/Downloads/MBSetup.exe")

print(age.st_mtime)
