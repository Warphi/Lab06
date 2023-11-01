# Jack Gordon

# display main menu
def displayMenu():
    print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
    """)

# encode the raw data by adding 3 to each number
def encode(raw):
    return "".join([str((int(c) + 3) % 10) for c in raw])

# decode the encoded data back to the original password by subtracting  3
def decode(password):
    raw = ''

    for i in range(len(password)):

        if (int(password[i])) < 3:
            digit = str(int(password[i]) + 7)
            raw += digit
        else:
            digit = str(int(password[i]) -3)
            raw += digit

    return raw

def main():
    encoded = ""

    while True:
        displayMenu()
        
        # input validation
        try:
            choice = input("Please enter an option: ")

            if int(choice) < 1 or int(choice) > 3:
                print("Invalid choice. Please try again")
                continue
        except:
            print("Invalid choice. Please try again")
            continue

        # encode
        if choice == "1":
            raw = input("Please enter your password to encode: ")
            encoded = encode(raw)
            print("Your password has been encoded and stored!")
        # decode
        if choice == "2":
            raw = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
        # quit
        if choice == "3":
            break

if __name__ == "__main__":
    main()
