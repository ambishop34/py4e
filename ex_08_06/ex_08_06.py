import urllib.request, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_578297.xml'
output = urllib.request.urlopen(url).read()
nathan = ET.fromstring(output)

sum = 0
for comments in nathan.findall('comments'):
    for comment in comments.findall('comment'):
        sum += int(comment.find('count').text)

print(sum)
