import urllib.request, urllib.error
import json

url = input('enter a url: ')
feedback = urllib.request.urlopen(urllib.request.Request(url)).read().decode('utf-8')
data = json.loads(feedback)
counts = list()

comments = data['comments']
for comment in comments:
    counts.append(comment['count'])
print(sum(counts))
