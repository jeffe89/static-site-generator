class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag      #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value  #A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children #A list of HTMLNode objects representing the children of this node
        self.props = props  #A dictionary of key-value pairs representing the attributes of the HTML tag.

    #Child classes will override this method to render themselves as HTML
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
        
    #return a string that represents the HTML attributes of the node.
    def props_to_html(self):
        if self.props == None:
            return ""
        
        #blank string for return
        props_html = ""

        #loop through dictionary to format all properties
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    # Returns a formatted string representation
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__ (tag, value, None, props)

    #return a string that represents the HTML attributes of the node.
    def to_html(self):
         #raise error if value equals None
         if self.value == None:
            raise ValueError("invalid HTML: no value")
         
         #return raw value if tag equals None
         if self.tag == None:
            return self.value
        
        #Otherwise, render an HTML tag
         return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    # Returns a formatted string representation
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
         
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    #return a string that represents the HTML attributes of the node.
    def to_html(self):
        #raise error if tag equals None
        if self.tag == None:
            raise ValueError("invalid HTML: no tag")
        
        #raise error if children equals None
        if self.children == None:
            raise ValueError("invalid HTML: no children")
        
        #otherwise, render HTML tag
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"