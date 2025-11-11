def gcd(a, b):
    while b != 0:
        remainder = a % b     
        a = b                 
        b = remainder         
    return a              

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))    
result = gcd(a, b)
print("GCD is:", result)