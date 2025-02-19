import unittest

from split_nodes import *
from extract_markdown import *
from split_nodes_delimiter import *
from text_to_textnodes import *
from textnode import *

class TestTextToTextNode(unittest.TestCase):
    def test_empty_text(self):
        # Test empty text
        text = ""
        nodes = text_to_textnodes(text)
        assert isinstance(nodes, list)
        assert len(nodes) == 0 

    def test_simple_text(self):
        # Test text with simple text
        text = "Hello, world"
        nodes = text_to_textnodes(text)
        assert isinstance(nodes, list)
        assert len(nodes) == 1 
        assert nodes[0].text == "Hello, world" 
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[0].url == None

    def test_bold_text(self):
        # Test text with bold markdown
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        assert isinstance(nodes, list)
        assert len(nodes) == 3 
        assert nodes[0].text == "This is " 
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[0].url == None
        assert nodes[1].text == "bold" 
        assert nodes[1].text_type == TextType.BOLD
        assert nodes[1].url == None
        assert nodes[2].text == " text" 
        assert nodes[2].text_type == TextType.TEXT
        assert nodes[2].url == None

    def test_italic_text(self):
        # Test text with italic markdown
        text = "This is *italic* text"
        nodes = text_to_textnodes(text)
        assert isinstance(nodes, list)
        assert len(nodes) == 3 
        assert nodes[0].text == "This is " 
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[0].url == None
        assert nodes[1].text == "italic" 
        assert nodes[1].text_type == TextType.ITALIC
        assert nodes[1].url == None
        assert nodes[2].text == " text" 
        assert nodes[2].text_type == TextType.TEXT
        assert nodes[2].url == None

    def test_code_text(self):
        # Test text with code markdown
        text = "This is `code` text"
        nodes = text_to_textnodes(text)
        assert isinstance(nodes, list)
        assert len(nodes) == 3 
        assert nodes[0].text == "This is " 
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[0].url == None
        assert nodes[1].text == "code" 
        assert nodes[1].text_type == TextType.CODE
        assert nodes[1].url == None
        assert nodes[2].text == " text" 
        assert nodes[2].text_type == TextType.TEXT
        assert nodes[2].url == None

    def test_image_text(self):
        # Test text with image markdown
        text = "This is an ![image](https://example.com/img.jpg) in text"
        nodes = text_to_textnodes(text)
        assert isinstance(nodes, list)
        assert len(nodes) == 3 
        assert nodes[0].text == "This is an " 
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[0].url == None
        assert nodes[1].text == "image" 
        assert nodes[1].text_type == TextType.IMAGE
        assert nodes[1].url == "https://example.com/img.jpg"
        assert nodes[2].text == " in text" 
        assert nodes[2].text_type == TextType.TEXT
        assert nodes[2].url == None

    def test_link_text(self):
        # Test text with link markdown
        text = "This is a [link](https://boot.dev) in text"
        nodes = text_to_textnodes(text)
        assert isinstance(nodes, list)
        assert len(nodes) == 3 
        assert nodes[0].text == "This is a " 
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[0].url == None
        assert nodes[1].text == "link" 
        assert nodes[1].text_type == TextType.LINK
        assert nodes[1].url == "https://boot.dev"
        assert nodes[2].text == " in text" 
        assert nodes[2].text_type == TextType.TEXT
        assert nodes[2].url == None

    def test_mult_markdown_text(self):
        # Test text with multiple markdown
        text = "This is **bold** and *italic* with a [link](https://boot.dev) and ![image](https://example.com/img.jpg)"
        nodes = text_to_textnodes(text)
        assert isinstance(nodes, list)
        assert len(nodes) == 8 
        assert nodes[0].text == "This is " 
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "bold" 
        assert nodes[1].text_type == TextType.BOLD
        assert nodes[2].text == " and " 
        assert nodes[2].text_type == TextType.TEXT
        assert nodes[3].text == "italic" 
        assert nodes[3].text_type == TextType.ITALIC
        assert nodes[4].text == " with a " 
        assert nodes[4].text_type == TextType.TEXT
        assert nodes[5].text == "link" 
        assert nodes[5].text_type == TextType.LINK
        assert nodes[5].url == "https://boot.dev"
        assert nodes[6].text == " and " 
        assert nodes[6].text_type == TextType.TEXT
        assert nodes[7].text == "image" 
        assert nodes[7].text_type == TextType.IMAGE
        assert nodes[7].url == "https://example.com/img.jpg"