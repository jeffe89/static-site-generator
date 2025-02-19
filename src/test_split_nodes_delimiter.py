import unittest
from split_nodes_delimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_no_delimiter(self):
        # Test 1: Node with no delimiters
        node1 = TextNode("Plain text", TextType.TEXT)
        nodes = split_nodes_delimiter([node1], "`", TextType.CODE)
        self.assertEqual(nodes, [TextNode("Plain text", TextType.TEXT)])

    def test_split_nodes_code_delim(self):
        # Test 2: Node with one pair of code delimiters
        node2 = TextNode("Text with `code` in it", TextType.TEXT)
        nodes = split_nodes_delimiter([node2], "`", TextType.CODE)
        self.assertEqual(nodes, [TextNode("Text with ", TextType.TEXT),
                                 TextNode("code", TextType.CODE),
                                 TextNode(" in it", TextType.TEXT)])
        
    def test_split_nodes_italic_delim(self):
        # Test 3: Node with one pair of italic delimiters
        node3 = TextNode("Text with *italics* in it", TextType.TEXT)
        nodes = split_nodes_delimiter([node3], "*", TextType.ITALIC)
        self.assertEqual(nodes, [TextNode("Text with ", TextType.TEXT),
                                 TextNode("italics", TextType.ITALIC),
                                 TextNode(" in it", TextType.TEXT)])
        
    def test_split_nodes_bold_delim(self):
        # Test 4: Node with one pair of bold delimiters
        node4 = TextNode("Text with **bold** in it", TextType.TEXT)
        nodes = split_nodes_delimiter([node4], "**", TextType.BOLD)
        self.assertEqual(nodes, [TextNode("Text with ", TextType.TEXT),
                                 TextNode("bold", TextType.BOLD),
                                 TextNode(" in it", TextType.TEXT)])

    def test_split_nodes_mult_delims(self):
        # Test 5: Multiple delimiter pairs
        node5 = TextNode("Text with `code` and `more code`", TextType.TEXT)
        nodes = split_nodes_delimiter([node5], "`", TextType.CODE)
        self.assertEqual(nodes, [TextNode("Text with ", TextType.TEXT),
                                 TextNode("code", TextType.CODE),
                                 TextNode(" and ", TextType.TEXT),
                                 TextNode("more code", TextType.CODE)])

    def test_unbalanced_delimiter(self):
        # Test 6: Unbalanced delimiters
        with self.assertRaises(Exception):
            node6 = TextNode("Text with `code only", TextType.TEXT)
            nodes = split_nodes_delimiter([node6], "`", TextType.CODE)

    def test_empty_delimiter(self):
        # Test 7: Empty delimiter content
        with self.assertRaises(Exception):
            node7 = TextNode("Text with `` empty", TextType.TEXT)
            nodes = split_nodes_delimiter([node7], "`", TextType.CODE)
          
    def test_non_text_node(self):
        # Test 8: Non-text nodes should pass through unchanged
        node8 = TextNode("**bold text**", TextType.BOLD)
        nodes = split_nodes_delimiter([node8], "`", TextType.CODE)
        self.assertEqual(nodes, [TextNode("**bold text**", TextType.BOLD)])
                                 