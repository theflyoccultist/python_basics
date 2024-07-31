add = lambda x , y : x + y
print(add(8,5))

def double(x):
    return x*2

sequence = [1, 3, 5, 9] 
doubled = [double(x) for x in sequence]
doubled2 = list(map(double, sequence))

print (doubled2)