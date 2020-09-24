#fname=input("Enater file name ")
handle=open("mbox-short.txt")
count=0
sum=0
for fy in handle:
    fy=fy.rstrip()
    if not fy.startswith("X-DSPAM-Confidence:") : continue
    #print(fy)
    nl=fy.find('0')
    #print(nl)
    n2=fy[20:]
    #print(n2)
    sum=float(n2)+sum
    count=count+1

#print(sum)
#print(count)
print('Average spam confidence:',sum/count)

print("Done")