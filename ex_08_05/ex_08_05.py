import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url: ')
link_line = int(input("Enter position: ")) - 1
#relative to first link
count = int(input("Enter count: "))

html = urllib.request.urlopen(url, context=ctx).read()
x = BeautifulSoup(html, 'html.parser')

while count >= 0:
   html = urllib.request.urlopen(url, context=ctx).read()
   x = BeautifulSoup(html, 'html.parser')
   tags = x('a')
   print(url)
   url = tags[link_line].get("href", None)
   count = count - 1
