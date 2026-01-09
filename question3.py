a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
c=int(input("enter the number c:"))

if a>b and a>c:
    print("a is greatest")
elif a<b and b>c:
    print("b is greatest")
else:
    print("c is greatest")