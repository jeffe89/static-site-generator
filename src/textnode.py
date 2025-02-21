from htmlnode import LeafNode
from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text    # Assigns the text content
        self.text_type = text_type  # Assigns the type of text (from the TextType Enum)
        self.url = url  # Assigns the URL, defaulting to None if not provided

    def __eq__(self, other):
        # Compares all properties to determine equality
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self):
        # Returns a formatted string representation
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    
def text_node_to_html_node(text_node):
    #Handle TextType.TEXT
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    #Handle TextType.BOLD
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    #Handle TextType.ITALIC
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    #Handle TextType.CODE
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    #Handle TextType.LINK
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    #Handle TextType.IMAGE
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    #Raise exception as TextType was not found
    raise ValueError(f"invalid text type: {text_node.text_type}")