from htmlnode import *
from textnode import *
from extract_markdown import *

def split_nodes_image(old_nodes):

    #Create empty list
    new_nodes = []

    #loop through each node in old_nodes list
    #Check if node is not a TextType.TEXT
    for node in old_nodes:
        if node.text_type != TextType.TEXT: #Append if not TextType.TEXT
            new_nodes.append(node)  
            continue

        #Otherwise, extract alt_text and URL
        image_tuple = extract_markdown_images(node.text)
        if not image_tuple:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        #Otherwise, split original text around image markdown and append to new_nodes
        for alt_text, url in image_tuple:
            sections = remaining_text.split(f"![{alt_text}]({url})", 1)
            # only append if text before image exists
            if sections[0]: 
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            # the image node always gets added since it has the alt_text    
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            # Update remaining_text for next iteration
            remaining_text = sections[1]

        #Append any remaining text after the last image
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
                    
    return new_nodes

def split_nodes_link(old_nodes):

    #Create empty list
    new_nodes = []

    #loop through each node in old_nodes list
    #Check if node is not a TextType.TEXT
    for node in old_nodes:
        if node.text_type != TextType.TEXT: #Append if not TextType.TEXT
            new_nodes.append(node)  
            continue

        #Otherwise, extract text and url
        link_tuple = extract_markdown_links(node.text)
        if not link_tuple:
            new_nodes.append(node)
            continue
            
        remaining_text = node.text
        #Otherwise, split original text around link markdown and append to new_nodes
        for text, url in link_tuple:
            sections = remaining_text.split(f"[{text}]({url})", 1)
            # only append if text before link exists
            if sections[0]: 
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            # the link node always gets added since it has the text   
            new_nodes.append(TextNode(text, TextType.LINK, url))
            # only append if text after link exists
            remaining_text = sections[1]
            
        #Append any remaining text after the last image
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
                    
    return new_nodes