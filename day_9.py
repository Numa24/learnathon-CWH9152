#sum of digits of a positive integer.
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage:
number = 12345
result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")

#reverse a string.
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Example usage:
text = "Hello, World!"
result = reverse_string(text)
print(f"The reversed string is: {result}")

#power of a number
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

result = power(2, 3)
print(result)