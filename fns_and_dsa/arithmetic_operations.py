# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations based on the operation parameter.

    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Type of operation ('add', 'subtract', 'multiply', 'divide')

    Returns:
        float | str: Result of the operation or an error message for invalid input
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Cannot divide by zero"
            return num1 / num2
        case _:
            return "Invalid operation"

