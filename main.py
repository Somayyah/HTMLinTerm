from myHTMLParser import MyHTMLParser
import sys
import requests
      
def main():
    url = ''
    if len(sys.argv) <= 1:
        url =  requests.get("http://0.0.0.0:8000")
    else:
        url =  requests.get(sys.argv[1])
    data = (url.content).decode()
    """     with open(file='./index.html', mode="r") as f:
            data = f.read()
    """    
    parser = MyHTMLParser()
    parser.feed(data=data)
    tree = parser.getDOMTree()
    if parser.getStackLen():
        print("Your HTML isn't properly formatted")
    if tree:
        tree.print_tree()

if __name__ == "__main__":
    main()


