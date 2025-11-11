import numpy as np

# Convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_nums(text):
    return [ord(c) - 65 for c in text.upper().replace(" ", "")]

# Convert numbers back to text
def nums_to_text(nums):
    return "".join(chr(n + 65) for n in nums)

# Encrypt using Hill cipher
def hill_encrypt(plaintext, key_matrix):
    nums = text_to_nums(plaintext)
    added_x = False
    if len(nums) % 2 != 0:
        nums.append(23)  # 'X'
        added_x = True

    nums = np.array(nums).reshape(-1, 2)#reshape for 2x2 matrix multiplication
    encrypted = (nums.dot(key_matrix) % 26).flatten()#flatten back to 1D array

    return nums_to_text(encrypted), added_x

# Decrypt using Hill cipher
def hill_decrypt(ciphertext, key_matrix, added_x):
    nums = text_to_nums(ciphertext)
    nums = np.array(nums).reshape(-1, 2)

    det = int(round(np.linalg.det(key_matrix)))
    det_inv = pow(det % 26, -1, 26)#modular inverse of determinant

    adj = np.array([[ key_matrix[1][1], -key_matrix[0][1]],
                    [-key_matrix[1][0],  key_matrix[0][0]]])

    inverse_matrix = (det_inv * adj) % 26
    decrypted = (nums.dot(inverse_matrix) % 26).flatten()
    decrypted_text = nums_to_text(decrypted)
    
    # Remove the added 'X' if it was added during encryption
    if added_x and decrypted_text[-1] == "X":
        decrypted_text = decrypted_text[:-1]
        
    return decrypted_text

# -----------------------------
# MAIN
# -----------------------------
key = [[3, 3],
       [2, 5]]   # Example invertible 2×2 Hill key

plaintext = input("Enter plaintext: ")
cipher, added_x = hill_encrypt(plaintext, key)
plain_back = hill_decrypt(cipher, key, added_x)

print("Encrypted:", cipher)
print("Decrypted:", plain_back)