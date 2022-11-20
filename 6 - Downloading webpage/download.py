import urllib.request
import sys
try:
    url,filename = sys.argv[1:3]
except ValueError:
    url="https://docs.python.org/3/library/urllib.html"
    filename="urllib.html"
urllib.request.urlretrieve(
    url,filename
)
for line in open(filename):
    print(line.strip())
