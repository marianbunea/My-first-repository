# HelloWorld.py
# This script prints a greeting and performs a simple calculator operation
# It also includes an exe file in the dist folder
# To create the exe, use the command: pyinstaller --onefile HelloWorld.py
import time

def pause(seconds):
    """Pause the execution for a given number of seconds.
    If seconds is 0 or less, it waits for user input to continue.
    """
    if seconds > 0:
        time.sleep(seconds)
    else:
        return input("Press Enter to continue...")

def simple_calculation(a, b, operation):
    """Perform a simple calculation based on the operation specified."""
    if operation == 'add':
        return int(a + b)
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b

print("Hello, nice to see you! This is my first py script in a git repo\n")
pause(1)

print("We will do a rudimentary calculator\n")
pause(1)

print("Please choose one of the following operations:")
pause(1)
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Desired operation (1-4): ")
print("Now, please enter two numbers:")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if operation == '1':
    print("Result= {}".format(simple_calculation(num1, num2, 'add'))) 
elif operation == '2':
    print("Result= {}".format(simple_calculation(num1, num2, 'subtract'))) 
elif operation == '3':
    print("Result={}".format(simple_calculation(num1, num2, 'multiply'))) 
elif operation == '4':
    while num2 == 0:
        num2 = float(input("You can't do that...Please enter a non-zero number for division: "))
    
    print("Result= {}".format(simple_calculation(num1, num2, 'divide'))) 

pause(2)
print("Thank you for using my calculator. Goodbye for now!")
pause(0)