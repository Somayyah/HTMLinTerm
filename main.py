from myHTMLParser import MyHTMLParser

def main():
    data = ''
    with open(file='./index.html', mode="r") as f:
        data = f.read()
    parser = MyHTMLParser()
    parser.feed(data=data)
    tree = parser.getDOMTree()
    if tree:
        tree.print_tree()

if __name__ == "__main__":
    main()


