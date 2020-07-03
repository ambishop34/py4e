import re

#hand = open("regex_sum_578293.txt")
#x=list()
#for line in hand:
     #y = re.findall('[0-9]+',line)
     #x = x+y

#sum=0
#for z in x:
    #sum = sum + int(z)

#print(sum)

file = open('regex_sum_578293.txt')
lst = list()
for line in file:
    line = line.rstrip()
    i = None
    i = re.findall('[0-9]+',line)
    lst = lst+i
#sum = 0
#for n in lst:
    #sum = sum + int(n)

print(lst)
