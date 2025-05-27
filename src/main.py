from textnode import TextNode
from textnode import TextType

def main():
    dummy_node = TextNode("anchor text", TextType.BOLD, "https://boot.dev")

    print(dummy_node)


main()