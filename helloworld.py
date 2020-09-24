largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        var=float(num)
    except:
        print("please try again")
        continue
    if largest is None:
        largest =var
    if smallest is None:
        smallest=var
    if largest < var:
        largest=var
    if smallest>var:
        smallest= var

    
    print('Largestso far ',largest,var)
    print('smallest so far ',smallest, var)


print("Maximum", largest)
print("smallest" ,smallest )