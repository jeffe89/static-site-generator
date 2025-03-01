import re

from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #Empty list to return
    new_nodes = []

    #Loop through old_nodes to check for TextTypes
    for old_node in old_nodes:

        #If TextType is TEXT, append as is to new_nodes
        if old_node.text_type != TextType.TEXT:  
            new_nodes.append(old_node)
            continue

        #Otherwise, split text, create nodes with corresponding TextType, add to new_nodes list
        split_nodes = []
        sections = old_node.text.split(delimiter)

        #Check length to determine if missing closing formatter
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        
        #Loop through each section of text
        for i in range(len(sections)):

            #if empty string continue
            if sections[i] == "":
                continue

            #If even section, append as text
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            #If odd, append with corresponding text_type
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        #Combine split_nodes into new_node        
        new_nodes.extend(split_nodes)

    #Return new_Nodes   
    return new_nodes
    
    
def split_nodes_image(old_nodes):
    #Create empty list
    new_nodes = []

    #loop through each node in old_nodes list
    #Check if node is not a TextType.TEXT
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            #Append if not TextType.TEXT
            new_nodes.append(old_node)
            continue

        #Store original_text    
        original_text = old_node.text

        #extract alt_text and URL
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        #split original text around image markdown and append to new_nodes
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)

            #Check to ensure correct markdown formatting
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            
            # only append if text before image exists
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            #Append image node    
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            # Update remaining_text for next iteration
            original_text = sections[1]

        #Append any remaining text after the last image    
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    #return new_nodes       
    return new_nodes    


def split_nodes_link(old_nodes):
    #Create empty list
    new_nodes = []

    #loop through each node in old_nodes list
    #Check if node is not a TextType.TEXT
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            #Append if not TextType.TEXT
            new_nodes.append(old_node)
            continue

        #Store original_text
        original_text = old_node.text

        #Extract text and url
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        #split original text around link markdown and append to new_nodes
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)

            #Check to ensure correct markdown formatting
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            
            # only append if text before link exists
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            #Append link node  
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            # Update remaining_text for next iteration
            original_text = sections[1]

        #Append any remaining text after the last link     
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    #return new_nodes        
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


