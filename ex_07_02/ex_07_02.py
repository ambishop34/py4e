fname = input("Enter a file name: ")
filehandle = open(fname)
first = list()
for line in filehandle:
    line = line.rstrip()
    line = line.split()
    for t in line:
        if not t in first:
            first.append(t)

first.sort()
print(first)
