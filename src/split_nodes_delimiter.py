from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        new_node = node.text.split(delimiter)
        if (len(new_node) - 1) % 2 != 0:
            raise SyntaxError("Invalid markdown syntax: must include both opening and closing delimiter")
        if len(new_node) > 1:
            for index, item in enumerate(new_node):
                if item == "":
                    continue
                if index % 2 != 0:
                    new_nodes.append(TextNode(item, text_type))
                else:
                    new_nodes.append(TextNode(item, TextType.TEXT))
        else:
            new_nodes.append(TextNode(new_node[0], TextType.TEXT))
    return new_nodes

