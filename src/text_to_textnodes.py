from split_nodes import *
from extract_markdown import *
from split_nodes_delimiter import *
from textnode import *

def text_to_textnodes(text):
    # Handle empty text case
    if not text: 
        return []

    # Start with a single text node
    nodes = [TextNode(text, TextType.TEXT)]

    # Process delimiters in sequence
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # Process images and links on all nodes at once
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes   