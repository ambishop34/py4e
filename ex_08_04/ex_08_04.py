import urllib.request
import re
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_578295.html').read()
sup = BeautifulSoup(html, "html.parser")

sum=0
# in the next two lines, we want to Retrieve all the anchor tags
tags = sup('span')
for tag in tags:

    y = str(tag)
    x = re.findall("[0-9]+",y)
    for i in x:
        i = int(i)
        sum = sum + i
print(sum)
