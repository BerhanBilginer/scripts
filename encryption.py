from cryptography.fernet import Fernet
import os

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt the contents of a file using the provided key
def encrypt_file(filename, key):
    cipher_suite = Fernet(key)  # Initialize a Fernet object with the encryption key
    with open(filename, 'rb') as file:
        plaintext = file.read()  # Read the plaintext data from the file
    encrypted_data = cipher_suite.encrypt(plaintext)  # Encrypt the plaintext data
    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)  # Write the encrypted data to a new file

# Generate an encryption key
key = generate_key()

# Specify the source file to be encrypted
 
source_path = "/media/berhan/CAA48122A48111DD/EDEFTER/5850031413/01.01.2022-31.12.2022/8/"

for file in os.listdir(source_path):
    os.chdir(source_path)
    if file.endswith(".xslt"):
        encrypt_file(file, key)
        source_file = file

# Inform the user about the successful encryption
print(f'{source_file} encrypted.')  # Print a message indicating successful encryption

# Print the encrypted content in hexadecimal format
encrypted_filename = source_file
with open(encrypted_filename, 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()
    encrypted = encrypted_data.hex()
    print("Encrypted Content:", encrypted)
