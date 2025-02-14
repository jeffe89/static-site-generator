import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode

# Add this debug print
print("Available TextTypes:", list(TextType))


class Test_function(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        node = TextNode("Hello, world!", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        assert html_node.tag is None
        assert html_node.value == "Hello, world!"

    def test_text_node_to_html_node_bold(self):
        node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "b"
        assert html_node.value == "Hello, world!"

    def test_text_node_to_html_node_italic(self):
        node = TextNode("Hello, world!", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "i"
        assert html_node.value == "Hello, world!"
    
    def test_text_node_to_html_node_code(self):
        node = TextNode("Hello, world!", TextType.CODE)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "code"
        assert html_node.value == "Hello, world!"

    def test_text_node_to_html_node_link(self):
        node = TextNode("Hello, world!", TextType.LINK, "boot.dev")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "a"
        assert html_node.props["href"] == "boot.dev"
        assert html_node.value == "Hello, world!"

    def test_text_node_to_html_node_image(self):
        node = TextNode("Hello, world!", TextType.IMAGE, "boot.dev")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props["src"] == "boot.dev"
        assert html_node.props["alt"] == "Hello, world!"

    def test_text_node_to_html_node_type_missing(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node("Not a test node")   
           