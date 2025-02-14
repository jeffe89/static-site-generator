from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
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