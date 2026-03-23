#pos,neg or zero ?
'''a=int(input("Enter a numbers"))
if a>0:
    print("its positive")
else :
    if a<0:
        print("its negative ")
    else :
        print("its zero")'''

# largest of three numbers 
'''a=int(input("Enter a numbers"))
b=int(input("Enter secound numbers"))
c=int(input("Enter third numbers"))
if a>b and a>c :
    print( a ,"is grater")
elif b>a and b>c:
    print(b ,"is the largest")
else :
    print(c ,"is the largest")'''

# factroal 
'''a=int(input("enter a number"))
f=1
i=1
while i<=a:
    f=f*i
    i=i+1
print("factroal of ",a," = ",f) '''
'''var = 10.5
if isinstance(var, float):
    print(f"{var} is a float")
else:
    print(f"{var} is not a float")'''
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
print(f"Sorted list: {numbers}")
print(type(numbers))


