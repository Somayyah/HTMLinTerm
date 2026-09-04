<<<<<<< HEAD
#!/usr/bin/env python

def main()
    pass
=======
from myHTMLParser import parser

def main():
    data = ''
    with open(file='./index.html', mode="r") as f:
        data = f.read()

    parser.feed(data=data)


if __name__ == "__main__":
    main()
>>>>>>> temp
