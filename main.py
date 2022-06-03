# Program will ask user to enter a string then asked what hash they want to use and then will print the hash

# Importing the hashlib library
import hashlib


# Defining the main function
def main():
    # Asking user to enter a string
    string = input("Enter a string: ")
    # print available hash functions
    print("Available hash functions:")
    print("md5\nsha1\nsha224\nsha256\nsha384\nsha512\nripemd160")
    # Asking user to enter a hash
    user_hash = input("Enter a hash: ")
    # Printing the hash
    try:
        print(hashlib.new(user_hash, string.encode()).hexdigest())
    except ValueError:
        print("Invalid hash")


# Loop the main function until the user wants to quit
while True:
    main()
    # Asking user if they want to quit
    if input("Do you want to quit? (y/n): ") == "y":
        break
