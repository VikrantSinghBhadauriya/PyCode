#fname = input("Enter file name: ")
fh = open("romeo.txt")
lst = list()
newlist=list()
for line in fh:
    #print(line.rstrip())
    #print(line.split())
    w=line.split()
    for word  in w:
            if word not in newlist:
                newlist.append(word)
#print(newlist)
newlist.sort()
print(newlist)
