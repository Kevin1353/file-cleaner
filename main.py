# Import required modules
import os
import time


# main function to call other functions
def main():
    path = get_path()
    age = get_age()
    file_list = get_file(path)
    for file in file_list:
        full_file = path + file  # this combines the file path with the specific file name
        file_age = is_file_old(full_file, age)
        if file_age == 1:
            delete_file(full_file)


# asks user to input a path for the folder they would like cleaned
def get_path():
    return input("Please enter the full file path to be cleaned (ex: C:/Users/kev12/Downloads/): ")


# asks user to input an age where they would like files to be deleted
def get_age():
    return int(input("How many days old must files be to be deleted: "))


# this gets the individual file that we will be using
def get_file(path):
    return os.listdir(path)  # this lists all files in a directory


# this function determines if a file is old enough that it should be deleted
def is_file_old(file, age):
    file_age = os.stat(file)
    seconds = time.time() - file_age.st_mtime  # this is the current seconds since Epoch minus the file's current
    # seconds since Epoch
    if age <= (((seconds/60)/60)/24):  # convert the seconds to days and compare to the expected age
        return 1


# this function deletes the given file
def delete_file(file):
    os.remove(file)


# call main
main()
