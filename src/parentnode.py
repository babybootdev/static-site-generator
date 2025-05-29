from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Every ParentNode must have a tag.")
        if self.children is None:
            raise ValueError("Every ParentNode must have children.")
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{html_string}</{self.tag}>"

    
