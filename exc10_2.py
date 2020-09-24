name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
y=list()
dic=dict()
for line in handle:
    if not line.startswith("From "):continue
    lst=line.split()
    temp=lst[5]
    print(lst)
    #lst=lst.split()
    print(temp)
    y=temp.split(':')
    print(y)
    z=y[0]
    print(y[0])
    if z not in dic:
        dic[z]=1
    else:
        dic[z]=dic[z]+1

print(dic)

tem=sorted(dic.items())
print(tem)
#s=sorted(tem)
#print(s)
for k,v in tem:
    print(k,v)
    
