from html.parser import HTMLParser
from domTree import Stack, Element, DOMTree

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.stack = Stack()
        self.domTree = None

    def handle_starttag(self, tag, attrs):
        element = Element(tag=tag, attributes=attrs)
        node = DOMTree(element)
        self.stack.push(node)
        if self.stack.top.next:
            self.stack.top.next.add_child(node)
        else:
            self.domTree = node
        if self.is_void_element(tag):
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag != "html":
            self.domTree = self.stack.top.next
        else:
            self.domTree = self.stack.top
        self.stack.pop()

    def handle_data(self, data):
        if not self.stack.is_empty():
            self.stack.top.root.data = data

    def handle_comment(self, data):
        """print("Comment  :", data)"""

    def handle_entityref(self, name):
        """c = chr(name2codepoint[name])
        print("Named ent:", c)"""

    def handle_charref(self, name):
        """if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)"""

    def handle_decl(self, data):
        """print("Decl     :", data)"""

    def is_void_element(self, tag):
        """Returns true if the tag is a self closing tag, which means it has no children"""
        return tag in ["area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"]
    
    def getDOMTree(self):
        return self.domTree