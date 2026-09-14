import sys
import html5lib
from contextlib import closing
import urllib.request as urllib2
from print_dom import print_dom

def main():
    url = ''
    if len(sys.argv) <= 1:
        url =  "http://0.0.0.0:8000"
    else:
        url =  sys.argv[1]
    data = ""
    with closing(urllib2.urlopen(url)) as f:
        parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("dom"))
        data = parser.parse(f, transport_encoding=f.info().get_content_charset())

    print_dom(data)

if __name__ == "__main__":
    main()


