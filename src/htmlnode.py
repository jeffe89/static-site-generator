class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag      #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value  #A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children #A list of HTMLNode objects representing the children of this node
        self.props = props  #A dictionary of key-value pairs representing the attributes of the HTML tag.

    def to_html(self):
        #Child classes will override this method to render themselves as HTML
        raise NotImplementedError
        
    def props_to_html(self):
        #return a string that represents the HTML attributes of the node.
        if self.props == None:
            return ""
        
        #blank string for return
        html_string = ""

        #loop through dictionary to format all properties
        for key in self.props:
            html_string += " " + key + '="' + self.props[key] + '"'
        return html_string
        
    def __repr__(self):
        # Returns a formatted string representation
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__ (tag, value, None, props)

    def to_html(self):
         #raise error if value equals None
         if self.value == None:
            raise ValueError
         
         #return raw value if tag equals None
         if self.tag == None:
            return self.value
        
        #Otherwise, render an HTML tag
         if self.props == None: 
            return f"<{self.tag}>{self.value}</{self.tag}>"
         else:
            prop_string = ""
            for key in self.props:
                prop_string += f' {key}="{self.props[key]}"'
            return f'<{self.tag}{prop_string}>{self.value}</{self.tag}>'
         
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        #raise error if tag equals None
        if self.tag == None:
            raise ValueError ("Tag value is None")
        
        #raise error if children equals None
        if self.children == None:
            raise ValueError ("Children value is None")
        
        #otherwise, render HTML tag
        #Check if props are available, if so add to html string
        if self.props != None:
            prop_string = ""
            for key in self.props:
                prop_string += f' {key}="{self.props[key]}"'
            html_string = f'<{self.tag}{prop_string}>'
        else:
            #otherwise, just render tag
            html_string = f"<{self.tag}>"

        #Loops through all children and call to_html() method
        for child in self.children:
            html_string += child.to_html()

        #add closing tag
        html_string += f"</{self.tag}>"

        #return html_string
        return html_string