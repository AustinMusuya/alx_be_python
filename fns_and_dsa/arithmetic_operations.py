"""
Create a Python script named arithmetic_operations.py. 
In this script, define a function that performs basic arithmetic operations. 
This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

Requirements for arithmetic_operations.py:
Function Definition:
Define a function named perform_operation.
Parameters: num1 (float), num2 (float), and operation (string). 

The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.

The function should execute the arithmetic operation 
based on the operation parameter and the numerical values provided.

For division, include handling for division by zero, 
returning a specific message or value that your main.py script can recognize and display appropriately.

Return the result of the arithmetic operation.

"""

def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num1 == 0 or num2 == 0:
                return("cannot divide by zero")
            else:
                result = num1 / num2

    return(result)

# math = perform_operation(0 , 4, 'divide')

# print(math)