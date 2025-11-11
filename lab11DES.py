# Simplified DES (S-DES) — সহজতম সংস্করণ
# কম কোড, কম চেক, built-in ব্যবহার, সরলতা বজায়।

def perm(bits, table):
    return ''.join(bits[i-1] for i in table)

def xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

# S-boxes
S0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]
S1 = [
    [0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]
]

def sbox(sbox, bits4):
    r = int(bits4[0] + bits4[3], 2)
    c = int(bits4[1] + bits4[2], 2)
    val = sbox[r][c]
    return f"{val:02b}"    # convert to 2-bit binary

# Key generation (simple)
def gen_keys(key):
    P10 = [3,5,2,7,4,10,1,9,8,6]
    P8  = [6,3,7,4,8,5,10,9]

    k = perm(key, P10)
    left, right = k[:5], k[5:]

    # LS-1
    left1 = left[1:] + left[:1]
    right1 = right[1:] + right[:1]
    k1 = perm(left1 + right1, P8)

    # LS-2
    left2 = left1[2:] + left1[:2]
    right2 = right1[2:] + right1[:2]
    k2 = perm(left2 + right2, P8)

    return k1, k2

# Round function
def f_function(bits, subkey):
    EP = [4,1,2,3,2,3,4,1]
    P4 = [2,4,3,1]

    left = bits[:4]
    right = bits[4:]

    ep = perm(right, EP)
    x = xor(ep, subkey)

    s0_out = sbox(S0, x[:4])
    s1_out = sbox(S1, x[4:])

    p4 = perm(s0_out + s1_out, P4)
    new_left = xor(left, p4)

    return new_left + right

# Encrypt
def sdes_encrypt(pt, key):
    IP = [2,6,3,1,4,8,5,7]
    IPi = [4,1,3,5,7,2,8,6]

    k1, k2 = gen_keys(key)

    ip = perm(pt, IP)
    r1 = f_function(ip, k1)
    swapped = r1[4:] + r1[:4]
    r2 = f_function(swapped, k2)
    cipher = perm(r2, IPi)
    return cipher

# Decrypt
def sdes_decrypt(ct, key):
    IP = [2,6,3,1,4,8,5,7]
    IPi = [4,1,3,5,7,2,8,6]

    k1, k2 = gen_keys(key)

    ip = perm(ct, IP)
    r1 = f_function(ip, k2)
    swapped = r1[4:] + r1[:4]
    r2 = f_function(swapped, k1)
    pt = perm(r2, IPi)
    return pt


# ------------ MAIN ------------
pt = input("Plaintext (8-bit): ")
key = input("Key (10-bit) : ")
keys=gen_keys(key)
print("Subkeys:", keys)
cipher = sdes_encrypt(pt, key)
plain_back = sdes_decrypt(cipher, key)

print("\nCiphertext =", cipher)
print("Decrypted  =", plain_back)
