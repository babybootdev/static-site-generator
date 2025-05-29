from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType):
    split_items = []
    new_type = TextType.TEXT

    match delimiter:
        case "`":
            new_type = TextType.CODE
        case "_":
            new_type = TextType.ITALIC
        case "**":
            new_type = TextType.BOLD
        case _:
            raise NotImplementedError("Other types have not yet been implemented.")

    for node in old_nodes:
        if node.text_type != TextType.TEXT or node.text.count(delimiter) == 0:
            split_items.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown syntax.")
        split_node = node.text.split(delimiter)

        for i, segment in enumerate(split_node):
            if (i == 0 or i == len(split_node) - 1) and segment == "":
                continue
            if i % 2 == 0:
                split_items.append(TextNode(segment, TextType.TEXT))
            else:
                split_items.append(TextNode(segment, new_type))
    return split_items

