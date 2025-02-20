import math
num=int(input("Enter a positive number:"))
root=math.sqrt(num)
if root.is_integer():
    print(f"{num} is perfect square")
else:
    print(f"{num} is not perfect sqaure")