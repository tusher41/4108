def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  #eta dar chek kora hoy abc kina symbol hole direct result a add kora hobe
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)#ord() function diye character er ASCII value ber kora hoyeche, tarpor shift add kore abar character e convert kora hoy chr() function diye
        else:
            result += char  
    return result

 
def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)  


message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted = caesar_encrypt(message, shift)
print(f"Encrypted message: {encrypted}")

decrypted = caesar_decrypt(encrypted, shift)
print(f"Decrypted message: {decrypted}")
