# Jack Gordon

# display main menu
def displayMenu():
    print("""
    1: Encode
    2: Decode
    """)

# encode the raw data by adding 3 to each number
def encode(raw):
    return "".join([str(int(c) + 3) for c in raw])

def main():
    print("Welcome to the encoder. Select an option below")

    while True:
        displayMenu()
        
        # input validation
        try:
            choice = input("Please enter your choice: ")

            if int(choice) != 1 or int(choice) != 2:
                print("Invalid choice. Please try again")
                continue
        except:
            print("Invalid choice. Please try again")
            continue

        # encode
        if choice == "1":
            raw = input("\nPlease enter string to be encoded: ")
            encoded = encode(raw)

            print("Encoded:", encoded)
        # decode
        if choice == "2":
            encoded = input("\n Please enter string to be decoded:")
            raw = decode(encoded)

            print("Decoded:", raw)

if __name__ == "__main__":
    main()