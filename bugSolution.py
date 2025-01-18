def function_with_uncommon_error(a, b):
    try:
        if isinstance(b, (int, float)) and b !=0:
          result = a / b
          return result
        else:
          raise TypeError("Unsupported operand type(s) for / ")
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example usage demonstrating both errors:
print(function_with_uncommon_error(10, 0))  # ZeroDivisionError
print(function_with_uncommon_error(10, 'a')) # TypeError
print(function_with_uncommon_error(10, 2)) #Correct Output