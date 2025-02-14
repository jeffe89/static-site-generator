from htmlnode import *
from textnode import *

def text_node_to_html_node(text_node):
    #Check if valid input
    if not isinstance(text_node, TextNode):
        raise ValueError("Expected TextNode")
    
    #Handle TextType.NORMAL
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    
    #Handle TextType.BOLD
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    #Handle TextType.ITALIC
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    #Handle TextType.CODE
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    #Handle TextType.LINK
    elif text_node.text_type == TextType.LINK:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
    
    #Handle TextType.IMAGE
    elif text_node.text_type == TextType.IMAGE:
        props = {
            "src": text_node.url,
            "alt": text_node.text
        }
        return LeafNode("img", "", props)
    
    #Raise exception as TextType was not found
    raise ValueError("Invalid text type")