#!/usr/bin/python3

from cryptography.fernet import Fernet
import sys


# Encrypt file
def encrypt_file(file):
    try:
        # Generates a key
        key = Fernet.generate_key()
        with open('thekey.key', 'wb') as f:
            f.write(key)
        # Encrypt
        with open(file, 'rb') as f:
            data = f.read()
        encrypted_data = Fernet(key).encrypt(data)
        # Write the encrypted data over the file 
        with open(file, 'wb') as f:
            f.write(encrypted_data)
    except Exception as e:
        print(f'[encrypt_file]\nError: {e}')


# Decrypt file
def decrypt_file(file):
    try:
        # Read key
        with open('thekey.key', 'rb') as key:
            secret_key = key.read()
        # Decrypt
        with open(file, 'rb') as f:
            data = f.read()
        decrypted_data = Fernet(secret_key).decrypt(data)
        # Write the decrypted data over the file
        with open(file, 'wb') as f:
            f.write(decrypted_data)
    except Exception as e:
        print('[decrypt_file]\nError: {e}')

# Main
def main():
    try:
        if len(sys.argv) != 3:
            print('./script <option> <file>')
        else:
            option = sys.argv[1]
            file = sys.argv[2]

            if option == 'enc':
                encrypt_file(file)
            elif option == 'dec':
                decrypt_file(file)
    except Exception as e:
        print('[main]\nError: {e}')

if __name__ == "__main__":
    main()


