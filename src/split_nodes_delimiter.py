from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    #Check for empty delimiter
    if not delimiter:
        raise Exception("Empty delimiter")
    
    #Empty list to return
    new_nodes = []

    #Loop through old_nodes to check for TextTypes
    for node in old_nodes:
        #If TextType is TEXT, append as is to new_nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node) 

        #Otherwise, split text, create nodes with corresponding TextType, add to new_nodes list         
        else:
            start = node.text.find(delimiter)  # Find first occurrence
            if start == -1: # No delimiter found
                new_nodes.append(node)
            else:
                end = node.text.find(delimiter, start + len(delimiter))  # Find next occurrence after start
                if end == -1:
                    raise Exception("Unbalanced delimiter")
                
                # Create three text nodes from the slices
                before = node.text[:start]  # before delimiter
                middle = node.text[start + len(delimiter):end]  # between delimiters
                after = node.text[end + len(delimiter):]  # after delimiter

                # Check for empty content between delimiters
                if not middle:
                    raise Exception("Empty delimiter content")

                # Append them (if not empty)
                if before:
                    new_nodes.append(TextNode(before, TextType.TEXT))
                if middle:
                    new_nodes.append(TextNode(middle, text_type))

                #Check for multiple delimiters     
                if after:
                    # Create a TextNode from 'after' text
                    after_node = TextNode(after, TextType.TEXT)
                    # Process it recursively and extend the results
                    new_nodes.extend(split_nodes_delimiter([after_node], delimiter, text_type))
                
    return new_nodes