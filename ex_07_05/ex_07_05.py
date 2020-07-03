name = input("Enter A file name:")
if len(name) < 1 :
     name = "mbox-short.txt"
handle = open(name, 'r')

hcount = dict()
list = []

for line in handle:
    words = line.split()
    if len(words) > 5 and words[0] == 'From':
        hr = words[5].split(':')
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1
    else:
        continue

for key,val in hcount.items():
    list.append((key,val))

list.sort()
for key,val in list:
    print(key,val)
