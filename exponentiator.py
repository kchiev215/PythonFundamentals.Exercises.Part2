def exponentiate(x,y):
    return x**y

def raise_to_fourth_power(x):
    return exponentiate(x,4)

square = lambda x: exponentiate(x,2)
cube = lambda x: exponentiate(x,3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))




