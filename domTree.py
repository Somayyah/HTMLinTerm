class Element:
    """A representation of the HTML element"""
    def __init__(self, tag, attributes = [], data = ""):
        self.data = data
        self.tag = tag 
        self.attributes = attributes
        self.next = None

    def __repr__(self):
        pass
        
class Stack:
    """A stack data structure to track the opened and closed HTML tags to pop them into the domTree"""
    def __init__(self):
        # self.value = value
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        pass

    def push(self, element):
        new_node = element
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        pop_value = self.top
        self.top = self.top.next
        self.size -= 1
        return pop_value

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.top

    def is_empty(self):
        return self.top is None

def is_there_whitespace(str):
    return str.isspace() or str == '' or str == "\n"

class DOMTree:
    def __init__(self, root=None):
        self.root = root
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        data_str = f", Data: {self.root.data}" if not is_there_whitespace(self.root.data) and self.root.tag not in ["script", "style", "img"] else ""
        print(prefix + self.root.tag + data_str)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level