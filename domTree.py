class Text:
    def __init__(self, text, parent):
        self.text = text
        self.children = []
        self.parent = parent

class Element:
    def __init__(self, tag, parent):
        self.tag = tag
        self.children = []
        self.parent = parent