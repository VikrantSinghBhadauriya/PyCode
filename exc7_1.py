fname=input("Enter file name")
handle=open(fname)
inp=handle.read()
inp=inp.rstrip()
inp=inp.upper()
print(inp)