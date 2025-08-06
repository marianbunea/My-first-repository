print("This is my first py script in a git repo\n")

print("Let's do a rudimentary calculator\n")

def simple_calculation(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Division by zero not possible"
        
print("Addition of number 8 and 2 is: {}".format(simple_calculation(8, 2, 'add')))
print("Subtraction of number 8 and 2 is: {}".format(simple_calculation(8, 2, 'subtract')))
print("Multiplication of number 8 and 2 is: {}".format(simple_calculation(8, 2, 'multiply')))
print("Division of number 8 and 2 is: {}".format(simple_calculation(8, 2, 'divide')))