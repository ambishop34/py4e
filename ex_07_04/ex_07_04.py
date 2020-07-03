name = input("Enter a file name:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    word = line.split()
    if line.startswith('From:'):
        count[word[1]] = count.get(word[1], 0) + 1
bigword = 0
highestemail = 0
for i in count:
    if count[i] > bigword:
        bigword = count[i]
        highestemail = i
print (highestemail, bigword)
