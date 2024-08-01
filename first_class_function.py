def divide(dividend, diviser):
    if diviser == 0:
        raise ZeroDivisionError("DIvisor cannot be 0.")
    
    return dividend/diviser

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)