import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!#$%&'()*+,-./@"

merged = lowercase + uppercase + digits + symbols

def password_gen(min_length, max_length):
    length = random.randint(min_length, max_length)
    password_lake = merged
    password = "".join(random.sample(password_lake, length))
    return password

def main():
    while True:
        try:
            min_length = int(input("Enter minimum password length (6 recommended): "))
            max_length = int(input("Enter maximum password length: "))

            if min_length < 6:
                print("Minimum password length must be at least 6 characters. Please try again.")
                continue

            if min_length > max_length:
                print("Minimum password length cannot be greater than maximum password length. Please try again.")
                continue

            num_passwords = int(input("Number of passwords to generate: "))

            for _ in range(num_passwords):
                password = password_gen(min_length, max_length)
                print(password)

            break

        except ValueError:
            print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()