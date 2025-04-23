# 1. Area of Rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area_rectangle = length * breadth
print(f"Area of rectangle = {area_rectangle}")

# 2. Area of Circle
import math
radius = float(input("\nEnter radius of circle: "))
area_circle = math.pi * radius ** 2
print(f"Area of circle = {area_circle}")

# 3. Marks in 5 Subjects - Total, Average, Percentage
print("\nEnter marks in 5 subjects:")
marks = [float(input(f"Subject {i+1}: ")) for i in range(5)]
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100
print(f"Total = {total}, Average = {average}, Percentage = {percentage}%")

# 4. Simple Interest and Amount
print("\nSimple Interest Calculation:")
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time in years: "))
simple_interest = (principal * rate * time) / 100
amount = principal + simple_interest
print(f"Simple Interest = {simple_interest}, Total Amount = {amount}")

# 5. Profit or Loss Calculation
print("\nProfit or Loss Calculation:")
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))
if sp > cp:
    profit = sp - cp
    print(f"Profit = {profit}")
elif cp > sp:
    loss = cp - sp
    print(f"Loss = {loss}")
else:
    print("No Profit No Loss")

# 6. Swap Two Numbers
print("\nSwap Two Numbers:")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"Before Swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After Swapping: a = {a}, b = {b}")
