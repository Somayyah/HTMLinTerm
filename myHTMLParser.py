from html.parser import HTMLParser
from html.entities import name2codepoint

class Element:
    """A class to represent the shape of an HTML element"""
    def __init__(self):
        self.name = ""
        self.attr = []
        self.styles = []
        
        
# named characters reference: https://html.spec.whatwg.org/entities.json
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_site_tree():
    
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

""" if __name__ == '__main__':
    build_product_tree()
 """    
class MyHTMLParser(HTMLParser):

    def __init__(self, *, convert_charrefs = True, scripting = False):
        super().__init__(convert_charrefs=convert_charrefs, scripting=scripting)
        self.root = None
        
    def handle_starttag(self, tag, attrs):
        if tag == 'html':
            self.root = TreeNode('html')
        elif tag in  ['body', 'head']:
            self.root.add_child(tag)

        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()