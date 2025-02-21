import os
import shutil

from textnode import *
from htmlnode import *
from markdown_blocks import *

def main():

    #Check path for public directory

    public_dir = "public"
    static_dir = "static"
    
    if os.path.exists(public_dir):
        #If found - remove directory
        shutil.rmtree(public_dir)

    #Recreate a public directory
    os.mkdir(public_dir)

    #Copy contents of static directory to public
    copy_static_contents(static_dir, public_dir)

    #Generate the index page
    from_path = "content"
    template_path = "template.html"
    generate_pages_recursive(from_path, template_path, public_dir)



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



def generate_page(from_path, template_path, dest_dir_path):

    # Get the filename from the path and change extension
    filename = os.path.basename(from_path)
    html_filename = filename.replace('.md', '.html')
    
    # Create the full destination path
    dest_path = os.path.join(dest_dir_path, html_filename)

    #Print details of generating page from path to dest path using template path
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #Read markdown file
    with open(from_path, 'r') as markdown_file:
        markdown_content = markdown_file.read()

    #Read template file
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    #Convert markdown to HTML
    markdown_html_node = markdown_to_html_node(markdown_content)
    html_content = markdown_html_node.to_html()

    #extract title
    title = extract_title(markdown_content)

    #Replace title and content placeholders in template.html
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_content)

    #Make directory to write the final template_content to using dest_path
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    #Write the final HTML to the destination file
    with open(dest_path, 'w') as dest_file:
        dest_file.write(template_content)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    #Print details of generating page from path to dest path using template path
    print(f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")

    #Create list containing all files / sub directories
    dir_list = os.listdir(dir_path_content)

    #Loop through each file / sub directory in list
    for entry in dir_list:

        #Create the full path to the entry
        full_path = os.path.join(dir_path_content, entry)

        #Check if its a file 
        if os.path.isfile(full_path) and full_path.endswith(".md"):
            generate_page(full_path, template_path, dest_dir_path)
        
        #Check if its a directory
        elif os.path.isdir(full_path):
            #Create the sub directory path in public
            dest_sub_path = os.path.join(dest_dir_path, entry)
            # Ensure directory exists
            os.makedirs(dest_sub_path, exist_ok=True)
            # Recursive call with new paths
            generate_pages_recursive(full_path, template_path, dest_sub_path)
    
        #If neither, skip it
        else:
            continue
            

if __name__ == "__main__":
    main()
