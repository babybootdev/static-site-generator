class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not yet implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        full_string = ""
        for key in self.props:
            full_string += f' {key}="{self.props[key]}"'
        return full_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

