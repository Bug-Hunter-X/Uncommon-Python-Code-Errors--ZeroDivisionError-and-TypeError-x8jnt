def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

# Example usage demonstrating both errors:
print(function_with_uncommon_error(10, 0))  # ZeroDivisionError
print(function_with_uncommon_error(10, 'a')) # TypeError