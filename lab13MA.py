# --- Helper Functions ---
def mod_exp(base, exponent, mod):
    """Modular exponentiation: (base^exponent) % mod"""
    return pow(base, exponent, mod)

def mod_add(a, b, mod):
    return (a + b) % mod

def mod_sub(a, b, mod):
    return (a - b) % mod

def mod_mul(a, b, mod):
    return (a * b) % mod

def mod_div(a, b, mod):
    """Modular division: a / b mod m, uses modular inverse"""
    b_inv = pow(b, -1, mod)
    return (a * b_inv) % mod

# --- Check Primitive Root ---
def is_primitive_root(g, p):
    required_set = set(range(1, p))
    actual_set = set(mod_exp(g, powers, p) for powers in range(1, p))
    return required_set == actual_set

# --- MAIN ---
p = int(input("Enter a prime number p: "))
g = int(input("Enter a primitive root modulo p: "))

if not is_primitive_root(g, p):
    print(f"{g} is not a primitive root modulo {p}")
else:
    print(f"{g} is a primitive root modulo {p}")
    
    # Example modular operations
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    
    print("Modular Addition:", mod_add(a, b, p))
    print("Modular Subtraction:", mod_sub(a, b, p))
    print("Modular Multiplication:", mod_mul(a, b, p))
    print("Modular Division:", mod_div(a, b, p))
    print("Modular Exponentiation a^b % p:", mod_exp(a, b, p))
