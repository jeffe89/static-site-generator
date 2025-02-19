import unittest
from extract_markdown import *
from split_nodes import *

class TestSplitNodesDelimiter(unittest.TestCase):
    ####IMAGE TESTS####
    def test_split_nodes_no_image(self):
        # Test 1: Node with no images
        node1 = TextNode("Just plain text", TextType.TEXT)
        nodes = split_nodes_image([node1])
        self.assertEqual(nodes, [TextNode("Just plain text", TextType.TEXT)])

    def test_split_nodes_one_image(self):
        # Test 2: Node with one image
        node2 = TextNode("Start ![image](https://example.com/img.png) end", TextType.TEXT)
        nodes = split_nodes_image([node2])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0], TextNode("Start ", TextType.TEXT))
        self.assertEqual(nodes[1], TextNode("image", TextType.IMAGE, "https://example.com/img.png"))
        self.assertEqual(nodes[2], TextNode(" end", TextType.TEXT))
        
    def test_split_nodes_image_non_text_type(self):
        # Test 3: Node that isn't TEXT type
        node3 = TextNode("![image](https://example.com/img.png)", TextType.BOLD)
        nodes = split_nodes_image([node3])
        self.assertEqual(nodes, [TextNode("![image](https://example.com/img.png)", TextType.BOLD)])

    def test_split_nodes_mult_image(self):
        # Test 4: Multiple images
        node4 = TextNode(
            "Start ![first](https://example.com/1.png) middle ![second](https://example.com/2.png) end",
            TextType.TEXT
        )
        nodes = split_nodes_image([node4])
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0], TextNode("Start ", TextType.TEXT))
        self.assertEqual(nodes[1], TextNode("first", TextType.IMAGE, "https://example.com/1.png"))
        self.assertEqual(nodes[2], TextNode(" middle ", TextType.TEXT))
        self.assertEqual(nodes[3], TextNode("second", TextType.IMAGE, "https://example.com/2.png"))
        self.assertEqual(nodes[4], TextNode(" end", TextType.TEXT))


    ####LINK TESTS####
    def test_split_nodes_no_link(self):
        # Test 1: Node with no links
        node1 = TextNode("Just plain text", TextType.TEXT)
        nodes = split_nodes_link([node1])
        self.assertEqual(nodes, [TextNode("Just plain text", TextType.TEXT)])

    def test_split_nodes_one_link(self):
        # Test 2: Node with one link
        node2 = TextNode("Click [here](https://boot.dev) to continue", TextType.TEXT)
        nodes = split_nodes_link([node2])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0], TextNode("Click ", TextType.TEXT))
        self.assertEqual(nodes[1], TextNode("here", TextType.LINK, "https://boot.dev"))
        self.assertEqual(nodes[2], TextNode(" to continue", TextType.TEXT))
        
    def test_split_nodes_link_non_text_type(self):
        # Test 3: Node that isn't TEXT type
        node3 = TextNode("[here](https://boot.dev)", TextType.BOLD)
        nodes = split_nodes_link([node3])
        self.assertEqual(nodes, [TextNode("[here](https://boot.dev)", TextType.BOLD)])

    def test_split_nodes_mult_link(self):
        # Test 4: Multiple links
        node4 = TextNode(
            "Visit [Boot.dev](https://boot.dev) and [GitHub](https://github.com)",
            TextType.TEXT
        )
        nodes = split_nodes_link([node4])
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0], TextNode("Visit ", TextType.TEXT))
        self.assertEqual(nodes[1], TextNode("Boot.dev", TextType.LINK, "https://boot.dev"))
        self.assertEqual(nodes[2], TextNode(" and ", TextType.TEXT))
        self.assertEqual(nodes[3], TextNode("GitHub", TextType.LINK, "https://github.com"))