#!/usr/bin/python

def encrypt(string, shift):
    cipher = ""
    for char in string:
        if char == " ":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr(
                (ord(char) + shift - 65) % 26 + 65
            )
        else:
            cipher = cipher + chr(
                (ord(char) + shift - 97) % 26 + 97
            )
    return cipher

def decrypt(string, shift):
    return encrypt(string,-shift)

if __name__ == "__main__":
    string = input("Enter the string to encrypt:")
    shift = int(input("Enter the shift number:"))
    print("Encrypted string:",encrypt(string,shift))
    string = input("Enter the string to decrypt:")
    shift = int(input("Enter the shift number:"))
    print("Decrypted string:",decrypt(string,shift))