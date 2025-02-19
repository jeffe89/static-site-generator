import unittest
from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        # Test 1: Extract markdown image
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        match = extract_markdown_images(text)
        self.assertEqual(match, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                                 ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_links(self):
        # Test 2: Extract markdown links
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        match = extract_markdown_links(text)
        self.assertEqual(match, [("to boot dev", "https://www.boot.dev"),
                                 ("to youtube", "https://www.youtube.com/@bootdotdev")])