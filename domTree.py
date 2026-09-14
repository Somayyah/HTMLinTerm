from xml.dom.minidom import Element, Document, Text

class ReprElement(Element):
    def __init__(self, tagName, namespaceURI = None, prefix = None, localName = None):
        super().__init__(tagName, namespaceURI, prefix, localName)

class ReprDocument(Document):
    def __init__(self):
        super().__init__()

class ReprText(Text):
    def __init__(self):
        super().__init__()


