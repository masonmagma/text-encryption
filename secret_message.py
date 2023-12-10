# imports the os module and Fernet class to the script
import os
from cryptography.fernet import Fernet

# Function that generates a key using the Fernet symmetric key encryption
def gen_key():
    return Fernet.generate_key()

# function used to write binary/encrypted data to a file using the parameters filename(name of file) and data(binary info to write to file)
def write_file(filename, data):
    with open(filename, 'wb') as file:   
        file.write(data)

# function to read and return binary contents of an encrypted file 
def read_file(filename):
    with open(filename, 'rb') as file:
        return file.read()
    
# function that takes a plaintext message from the user and selected key of choice and returns the message encoded
def encrypt_message(message, key):
    cipher = Fernet(key)                                    #creates a Fernet object named cipher with key of choice for encryption tasks
    encrypted_message = cipher.encrypt(message.encode())    #converts message to bytes and calls upon the cipher to convert an encrypted message
    return encrypted_message

# function takes encrypted message and selected key as parameters to then return message decrypted (plaintext)
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)                                    # creates Fernet object of chosen key
    decrypted_message = cipher.decrypt(encrypted_message).decode()      # cipher.decrypt decrypts message using key object, .decode() converts decrypted bytes to string format
    return decrypted_message



#main block of code for user operations in the CLI
print("")
print("###########################################################")
print("Welcome to Mason's Secret Message encryption/decryption CLI")
print("###########################################################")
print("")

# Prompts user to generate a new key or input a previous key
key_choice = input("Do you want to generate a new key? (y/n) select (n) to enter your own key: ").lower()
if key_choice == 'y':
    key = gen_key()
    key = gen_key()
    key_string = key.decode()  # Convert bytes to a string to display new key to user

    print(f"Your Generated key is: {key_string}") # prints new generated key so user can record key
    print("don't forget your key!")
    print("")
else:
    key = input("Enter your key: ")   

# Choose between encryption and decryption
operation = input("Please choose to encrypt (e) or decrypt (d) a message?: ").lower()

if operation == 'e':
    # Prompts user to input message and filename
    message = input("Enter your secret message: ")
    filename = input("Enter the Filename of your encrypted message: ")

    # calls upon encypt_message and write_file functions to encrypt the message and write encypted message to a file
    encrypted_message = encrypt_message(message, key)
    write_file(filename, encrypted_message)

    print(f"Your secret message has been encrypted and saved to {filename}")

elif operation == 'd':
    # Input filename to read encrypted message from
    filename = input("Enter the filename with the encrypted message: ")

    # Read and decrypt message from file
    encrypted_message = read_file(filename)
    decrypted_message = decrypt_message(encrypted_message, key)

    print(f"Your secret decrypted message is: {decrypted_message}")

else:      #prompts user that an invalid input was made                                                                          
    print("Invalid response. Please choose 'e' for encryption or 'd' for decryption.")
