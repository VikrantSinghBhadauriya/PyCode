#fname=input("Enater file name ")
handle=open("mbox-short.txt")
dic=dict()
lst=list()
count=0
for line in handle:
    line=line.rstrip()
    if not line.startswith("From "):continue
    lst = line.split()
    lst=lst[1]
    
    #print(lst)
    #for words in lst:
    if lst not in dic:
            dic[lst]=1
    else:
            dic[lst]=dic[lst]+1
#print(dic)
largekey=None
largevalue=None
for key,value in dic.items():
    if largevalue is None or largevalue<value:
            largevalue=value
            largekey=key
print(largekey,largevalue)


 