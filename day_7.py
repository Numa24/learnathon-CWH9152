#multiplicaion table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#Sum of Even Numbers
sum_even = 0
counter = 2

while counter <= 50:
    sum_even += counter
    counter += 2

print("Sum of even numbers from 1 to 50:", sum_even)

# Factorial Calculation
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is: {factorial}")

# * pattern
for i in range(1, 7):
    for j in range(i):
        print("*", end="")
    print()

#prime no.
num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")