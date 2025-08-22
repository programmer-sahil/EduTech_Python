# Factorial of a Number (n= 5)
# 1*2*3*4*5 = 120
n =5
fact = 1
for i in range(1, n+1):
    fact = fact * i    # fact *= i

print(f"The factorial is: {fact}")