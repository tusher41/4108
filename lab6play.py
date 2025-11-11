def playfair(key, text, encrypt=True):
    # Prepare key and matrix
    key = "".join(dict.fromkeys(key.upper().replace("J","I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
    matrix = [key[i:i+5] for i in range(0,25,5)]
    
    # Prepare text
    text = text.upper().replace("J","I")
    text = "".join(c for c in text if c.isalpha())
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) and text[i+1] != a else "X"
        pairs.append(a + b)
        i += 2 if i+1 < len(text) and text[i+1] != a else 1
    
    # Encrypt/decrypt
    result = []
    shift = 1 if encrypt else -1
    for a,b in pairs:
        row1, col1 = divmod(key.index(a), 5)
        row2, col2 = divmod(key.index(b), 5)
        if row1 == row2:
            result.append(matrix[row1][(col1+shift)%5] + matrix[row2][(col2+shift)%5])
        elif col1 == col2:
            result.append(matrix[(row1+shift)%5][col1] + matrix[(row2+shift)%5][col2])
        else:
            result.append(matrix[row1][col2] + matrix[row2][col1])
    
    return "".join(result)
def clean(text):
    return text.replace("X", "")
# Usage
key = input("Enter key: ").upper().replace("J","I")
text = input("Enter text: ").upper().replace("J","I")
encrypted = playfair(key, text, encrypt=True)
decrypted = clean(playfair(key, encrypted, encrypt=False))

print(f"Text: {text}")
print(f"Encrypted: {encrypted}") 
print(f"Decrypted: {decrypted}")