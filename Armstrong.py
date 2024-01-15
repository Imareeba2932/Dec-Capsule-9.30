i = int(input("Enter a number: "))
orig = i
sum = 0
while i > 0:
    sum = sum+(i % 10) ** 3
    i //= 10 
if sum == orig:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")