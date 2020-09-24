#fname=input("Enater file name ")
handle=open("mbox-short.txt")
lst=list()
count=0
for line in handle:
   line=line.rstrip()
   if not line.startswith("From "):continue
   print(line)
   lst=line.split()
   #print(lst[1]) 
   count+=1

print("There were", count, "lines in the file with From as the first word")

