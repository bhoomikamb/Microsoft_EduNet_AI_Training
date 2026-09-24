x=int(input("Enter a number:"))
y=int(input("enter another number:"))
if x>y:
    print("x is largest!!")
    print(f"{x} is greater than {y}")
elif x<y:
    print("y is largest!!")
    print(f"{y} is greater than {x}")
else:
    print("Both numbers are equal!!")
    print(f"{x} is equal to {y}")