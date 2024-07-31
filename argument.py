def add(x, y):
    return x + y

num = [3, 5]
add(*num)

numz = {"x": 15, "y": 26}
print(add(**numz))

def multiply(*argz):
    total = 1
    for arg in argz:
        total = total * arg

    return total

def apply(*argz, operator):
    if operator == "*":
        return multiply(*argz)
    elif operator == "+":
        return sum(argz)
    else:
        return "no valid operator detected."
    
print(apply(1, 3, 5, 7, operator="+"))