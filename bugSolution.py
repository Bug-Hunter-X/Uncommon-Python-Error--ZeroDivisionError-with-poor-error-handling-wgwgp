def function_with_improved_error_handling(x):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return x + 5
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None  # Or handle the error in a more appropriate way for your application