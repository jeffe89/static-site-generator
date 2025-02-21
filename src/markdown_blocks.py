from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node



class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quite"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def markdown_to_blocks(markdown):
    #Split markdown into separate blocks
    blocks = markdown.split("\n\n")

    #Create empty list
    filtered_blocks = []

    #Loop through each block
    for block in blocks:
        #if empty string, continue
        if block == "":
            continue

        #Strip off any whitespace
        block = block.strip()

        #Append to filtered_blocks list
        filtered_blocks.append(block)

    #REturn filtered_blocks list   
    return filtered_blocks


def block_to_block_type(block):

    #split block into separate lines
    lines = block.split("\n")

    #Check for HEADING BlockType
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    #Check for CODE BlockType
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    #Check for QUOTE BlockType
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    #Check for ULIST BlockType
    #Starts with '*'
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    #Check for ULIST BlockType
    #Starts with '-'
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    #Check for OLIST BlockType
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    
    #Otherwise, return PARAGRAPH BlockType
    else:
        return BlockType.PARAGRAPH
    

def markdown_to_html_node(markdown):
    #Create a list of blocks from markdown
    blocks = markdown_to_blocks(markdown)

    #Create empty list
    children = []

    #Loop through each block
    for block in blocks:
        #Convert block to HTMLNode
        html_node = block_to_html_node(block)
        
        #Append to children list
        children.append(html_node)

    #Return ParentNode    
    return ParentNode("div", children, None)
    

def block_to_html_node(block):
    #Find the BlockType of block passed as parameter
    block_type = block_to_block_type(block)

    #PARAGRAPH BlockType
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    
    #HEADING BlockType
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    
    #CODE BlockType
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    
    #OLIST BlockType
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    
    #ULIST BlockType
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    
    #QUOTE BlockType
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    
    #Error if invalid BlockType
    raise ValueError("invalid block type")

#Helper function to convert TextNode to HTMLNode
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

#Helper function to handle PARAGRAPH block
def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

#Helper function to handle HEADING block
def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

#Helper function to handle CODE block
def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

#Helper function to handle OLIST block
def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

#Helper function to handle ULIST block
def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

#Helper function to handle QUOTE block
def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)