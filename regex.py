import re
name=input("Enter file Name")
handle=open('origin.txt')
file=handle.read()
total=0
print(file)
y=re.findall('[0-9]+',file)
print(y)
for nums in y:
    total=int(nums)+total
print(total)