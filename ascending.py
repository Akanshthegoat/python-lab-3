num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1<=num2 and num1<=num3:
    print(f"\n ascending: {num1},{min(num2,num3)},{max(num2,num3)}")
elif num2<=num1 and num2<=num3:
    print(f"\n ascending: {num2},{min(num1,num3)},{max(num1,num3)}")
else:
    print(f"\n ascending: {num3},{min(num2,num1)},{max(num2,num1)}")



