from textnode import *
from htmlnode import *

import os
import shutil

def main():

    #Check path for public directory

    public_dir = "/home/jepp/workspace/github.com/jeffe89/static-site-generator/public"
    static_dir = "/home/jepp/workspace/github.com/jeffe89/static-site-generator/static"
    
    if os.path.exists(public_dir):
        #If found - remove directory
        shutil.rmtree(public_dir)

    #Recreate a public directory
    os.mkdir(public_dir)

    #Copy contents of static directory to public
    copy_static_contents(static_dir, public_dir)


def copy_static_contents(source, destination):
    #Create list containing all files / sub directories
    static_dir_list = os.listdir(source)

    #Traverse the static directory list
    for file in static_dir_list:

        #Gather the source path for individual file / sub directory
        source_path = os.path.join(source, file)
        
        #If source path is to a file
        if os.path.isfile(source_path):
            destination_path = os.path.join(destination, file)
            shutil.copy(source_path, destination_path)
        
        #If source path is to a sub directory, crete corresponding directory in public
        else:
            destination_path = os.path.join(destination, file)
            os.mkdir(destination_path)
            copy_static_contents(source_path, destination_path)

if __name__ == "__main__":
    main()
