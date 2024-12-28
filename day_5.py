#IF STATEMENT
number = int(input('Enter a number: '))
# check if number is greater than 0
if number > 0:
    print(f'{number} is a positive number.')

print('A statement outside the if statement.')

#IF ELSE
number = int(input('Enter a number: '))
if number > 0:
    print('Positive number')
else:
    print('Not a positive number')
print('This statement always executes')

#ELIF
number = -5

if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')

print('This statement is always executed')

#NESTED IF
number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')


  #2  
score = float(input("Enter the exam score: "))

if score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")

#leap yr
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#bonus
age = int(input("Enter your age: "))
show_time = int(input("Enter the show time (in 24-hour format): "))

match age:
    case 0 | 1 | 2 | 3 | 4 | 5:
       ticket_price =  0  # Free ticket for ages 0-5
    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
       ticket_price =  100  # Rs.100 ticket for ages 6-12
    case 13 | 14 | 15 | 16 | 17 | 18:
       ticket_price =  250  # Rs.250 ticket for ages 13-18
    case _:
       ticket_price =  280  # Rs.280 ticket for age 19 and above

# Apply discount for shows before 12:00 PM
if show_time < 12:
    ticket_price -= 5

print(f"The ticket price is Rs.{ticket_price}.")
