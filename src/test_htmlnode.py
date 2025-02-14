import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')


class TestLeafNode(unittest.TestCase):
    def test_basic_tag(self):
        node = LeafNode("p", "Hello")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_with_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "class": "link"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" class="link">Click me!</a>')

    def test_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()


class TestParentNode(unittest.TestCase):

    def test_parent_node(self):
        node = ParentNode(
            "div",
            [
                LeafNode("span", "child1"),
                LeafNode("span", "child2")
            ]
        )
        self.assertEqual(node.to_html(), "<div><span>child1</span><span>child2</span></div>")

    def test_parent_with_props(self):
        node = ParentNode(
            "div",
                [LeafNode("p", "hello")],
                {"class": "greeting"}
        )
        self.assertEqual(node.to_html(), '<div class="greeting"><p>hello</p></div>')

    # Test 3: Nested parents
    def test_nested_parent(self):
        node = ParentNode(
            "div",
                [
                ParentNode(
                    "p",
                    [LeafNode("span", "nested")]
                )
                ]
        )
        self.assertEqual(node.to_html(), "<div><p><span>nested</span></p></div>")



if __name__ == "__main__":
    unittest.main()