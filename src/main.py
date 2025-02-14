from textnode import *
from htmlnode import *

def main():

    test_text_node = TextNode("this is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_text_node)
    
    node = HTMLNode(props={"href": "https://www.google.com"})
    print(node.props_to_html())

    node2 = HTMLNode()
    print(node2.props_to_html())
    
    
if __name__ == "__main__":
    main()
