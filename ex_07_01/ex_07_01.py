filehandle = open('words-short.txt')

for t in filehandle:
    filehandle = t.rstrip()
    print (filehandle.upper())
