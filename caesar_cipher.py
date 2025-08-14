def welcome():
    print("Welcome to the Caesar Cipher program!")

def enter_message():
    mode = ""
    while mode != "encrypt" and mode != "decrypt":
        mode = input("Enter mode (encrypt/decrypt): ").lower()
    message = input("Enter message: ").upper()
    return mode, message

def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            char_code += shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            encrypted_message += chr(char_code)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            char_code -= shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            decrypted_message += chr(char_code)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    welcome()
    while True:
        mode, message = enter_message()
        shift = int(input("Enter shift number: "))
        if mode == "encrypt":
            print("Encrypted message: ", encrypt(message, shift))
        elif mode == "decrypt":
            print("Decrypted message: ", decrypt(message, shift))
        choice = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if choice != "y":
            break

if __name__ == "__main__":
    main()
    