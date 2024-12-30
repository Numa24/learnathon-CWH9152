# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)

#RETURN STATEMENT
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)
#return statement also denotes that the function has ended. Any code after return is not executed.
def future_function():
    pass

# this will execute without any action or error
future_function()  

import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)

#sum
def sum_numbers(num1, num2):
    return num1 + num2


result = sum_numbers(10, 20)
print("Sum: {result}")

#grade_converter

def grade_converter(numerical_grade):
    if numerical_grade >= 90:
        return 'A'
    elif numerical_grade >= 80:
        return 'B'
    elif numerical_grade >= 70:
        return 'C'
    elif numerical_grade >= 50:
        return 'D'
    else:
        return 'F'


letter_grade = grade_converter(85)
print("Letter Grade: {letter_grade}")

#3
def outer_function():
    x = 10  # Variable in the outer function's scope
    
    def inner_function():
        y = 5  # Variable in the inner function's scope
        return x + y  # Accessing x from the outer function's scope
    
    result = inner_function()
    return result

# Example Usage:
result_value = outer_function()
print("Result: {result_value}") 
