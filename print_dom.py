import xml.dom.minidom as minidom

def print_dom(node, depth=0):
    """Print a minidom DOM as an indented tree."""
    prefix = ("   " * depth + "|__") if depth else ""
    if node.nodeType == minidom.Node.DOCUMENT_NODE:
        if node.documentElement is not None:
            print_dom(node.documentElement, depth)
    elif node.nodeType == minidom.Node.ELEMENT_NODE:
        tag = node.localName or node.tagName
        print(prefix + tag)
        for child in node.childNodes:
            print_dom(child, depth + 1)
    elif node.nodeType == minidom.Node.TEXT_NODE:
        text = node.data.strip()
        if text:
            print("   " * depth + f'"{text}"')
    elif node.nodeType == minidom.Node.COMMENT_NODE:
        print("   " * depth + f"<!--{node.data}-->")